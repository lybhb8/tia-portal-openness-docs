"""
Sphinx 文档构建测试
测试文档是否能正确构建
"""
import pytest
from pathlib import Path
from sphinx.testing.util import SphinxTestApp


@pytest.fixture(scope="session")
def app():
    """创建 Sphinx 应用"""
    root = Path(__file__).parent.parent
    srcdir = root / "docs"
    confoverrides = {"master_doc": "index"}

    app = SphinxTestApp(
        buildername="html",
        srcdir=srcdir,
        confoverrides=confoverrides,
    )
    yield app
    app.cleanup()


def test_build_success(app):
    """测试文档构建成功"""
    # 构建文档
    app.build()

    # 检查构建状态
    assert app.statuscode == 0, f"构建失败: {app.stdout()}"


def test_index_html_exists(app):
    """测试 index.html 生成"""
    app.build()
    index_html = app.outdir / "index.html"
    assert index_html.exists(), "index.html 未生成"


def test_chapters_html_exists(app):
    """测试章节 HTML 文件生成"""
    app.build()

    expected_files = [
        "chapter_01_1-网络安全信息.html",
        "chapter_02_2-TIA-Portal-Openness-自述文件.html",
        "chapter_03_3-TIA-Portal-Openness-中的新功能.html",
        "chapter_04_4-基本知识.html",
        "chapter_05_5-TIA-Portal-Openness-API.html",
        "chapter_06_6-导出导入.html",
        "chapter_07_7-主要变化.html",
    ]

    for filename in expected_files:
        html_file = app.outdir / filename
        assert html_file.exists(), f"{filename} 未生成"


def test_output_not_empty(app):
    """测试输出目录不为空"""
    app.build()
    output_files = list(app.outdir.glob("*.html"))
    assert len(output_files) > 0, "输出目录为空"
