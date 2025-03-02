import os
import pytest
from unittest.mock import MagicMock
from main import run_answer_anything_system, setup_output_dirs, sanitize_folder_name

# 測試 sanitize_folder_name 函數
def test_sanitize_folder_name():
    assert sanitize_folder_name("AI是否會取代人類的工作？") == "AI是否會取代人類的工作？"
    assert sanitize_folder_name('a b:c*d?e"f<g>h|i') == "a_bcdefghi"
    assert sanitize_folder_name("  hello  world  ") == "hello_world"

# 測試 setup_output_dirs 函數
def test_setup_output_dirs(tmpdir):
    base_dir = tmpdir.mkdir("output")
    dirs = setup_output_dirs(base_dir)
    
    assert os.path.exists(dirs["stage1"])
    assert os.path.exists(dirs["stage2"])
    assert os.path.exists(dirs["stage3"])

# 測試 run_answer_anything_system 函數
def test_run_answer_anything_system(mocker):
    # 模擬 AnalyzeAgent
    mock_analyzer = mocker.patch("main.AnalyzeAgent")
    mock_analyzer_instance = mock_analyzer.return_value
    mock_analyzer_instance.opposite_opinion_association.return_value = "反面觀點"
    mock_analyzer_instance.analyze_critique.return_value = "批判分析"
    mock_analyzer_instance.analyze_significance.return_value = "現實意義分析"

    # 模擬 DebatorAgent
    mock_debator = mocker.patch("main.DebatorAgent")
    mock_debator_instance = mock_debator.return_value
    mock_debator_instance.generate_argument.return_value = "生成觀點"

    # 模擬 ExpressAgent
    mock_expresser = mocker.patch("main.ExpressAgent")
    mock_expresser_instance = mock_expresser.return_value
    mock_expresser_instance.build_golden_sentence.return_value = "金句"
    mock_expresser_instance.build_self_expression.return_value = "自我表達"

    # 模擬文件讀取
    mocker.patch("builtins.open", mocker.mock_open(read_data="自我表達"))

    # 運行測試
    topic, response = run_answer_anything_system("AI是否會取代人類的工作？")

    # 驗證結果
    assert topic == "AI是否會取代人類的工作？"
    assert response == "自我表達"

    # 驗證 AnalyzeAgent 的方法是否被調用
    mock_analyzer_instance.opposite_opinion_association.assert_called_once_with("AI是否會取代人類的工作？")
    mock_analyzer_instance.analyze_critique.assert_called_once()
    mock_analyzer_instance.analyze_significance.assert_called_once_with("AI是否會取代人類的工作？")

    # 驗證 DebatorAgent 的方法是否被調用
    mock_debator_instance.generate_argument.assert_called_once_with("AI是否會取代人類的工作？")

    # 驗證 ExpressAgent 的方法是否被調用
    mock_expresser_instance.build_golden_sentence.assert_called_once_with("AI是否會取代人類的工作？")
    mock_expresser_instance.build_self_expression.assert_called_once_with("AI是否會取代人類的工作？")
    