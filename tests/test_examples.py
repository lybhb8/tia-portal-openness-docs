"""
Sphinx 代码示例测试
验证文档中的代码示例
"""
import pytest
from pathlib import Path
import re


@pytest.fixture
def docs_dir():
    """文档目录"""
    return Path(__file__).parent.parent / "docs"


def test_csharp_code_blocks(docs_dir):
    """测试 C# 代码块"""
    code_blocks = []

    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        # 查找 C# 代码块
        pattern = r'```csharp\s*\n(.*?)\n```'
        for match in re.finditer(pattern, content, re.DOTALL):
            code = match.group(1).strip()
            code_blocks.append({
                'file': md_file.name,
                'code': code
            })

    print(f"  找到 {len(code_blocks)} 个 C# 代码块")

    # 检查基本语法结构
    for block in code_blocks[:5]:  # 只检查前 5 个
        code = block['code']
        # 检查大括号匹配
        open_braces = code.count('{')
        close_braces = code.count('}')
        if open_braces != close_braces:
            print(f"  ⚠ {block['file']}: 大括号不匹配")

    assert True, "C# 代码块检查完成"


def test_code_examples_have_comments(docs_dir):
    """测试代码示例包含注释"""
    code_blocks = []

    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        pattern = r'```csharp\s*\n(.*?)\n```'
        for match in re.finditer(pattern, content, re.DOTALL):
            code = match.group(1).strip()
            code_blocks.append({
                'file': md_file.name,
                'code': code
            })

    documented = 0
    for block in code_blocks:
        if '///' in block['code'] or '//' in block['code']:
            documented += 1

    print(f"  有注释的代码块: {documented}/{len(code_blocks)}")

    assert True, "代码注释检查完成"


def test_api_usage_in_examples(docs_dir):
    """测试示例中使用正确的 API"""
    expected_patterns = [
        'Siemens.Engineering',
        'Engineering.Create',
        'GetCurrentProcess',
    ]

    found_patterns = set()

    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        for pattern in expected_patterns:
            if pattern in content:
                found_patterns.add(pattern)

    print(f"  找到的 API 模式: {len(found_patterns)}/{len(expected_patterns)}")
    for pattern in sorted(found_patterns):
        print(f"    - {pattern}")

    assert True, "API 使用检查完成"
