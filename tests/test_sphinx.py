"""
Sphinx 文档测试配置
使用 sphinx.testing 框架进行本地测试
"""
import pytest
from pathlib import Path

# 项目根目录
ROOT = Path(__file__).parent.parent
DOCS = ROOT / "docs"
CONF = ROOT / "conf.py"


@pytest.fixture(scope="session")
def srcdir():
    """文档源目录"""
    return DOCS


@pytest.fixture(scope="session")
def confdir():
    """配置文件目录"""
    return ROOT


@pytest.fixture(scope="session")
def make_app(mocker, srcdir, confdir):
    """创建 Sphinx 应用"""
    from sphinx.testing.util import SphinxTestApp

    # 创建临时构建目录
    build_dir = ROOT / "_build"
    build_dir.mkdir(exist_ok=True)

    # 配置 SphinxTestApp
    app = SphinxTestApp(
        buildername="html",
        srcdir=srcdir,
        confoverrides={"master_doc": "index"},
    )
    return app


def test_index_exists(make_app):
    """测试 index.md 存在"""
    index = make_app.srcdir / "index.md"
    assert index.exists(), "index.md 不存在"


def test_chapters_exist(make_app):
    """测试所有章节文件存在"""
    expected_chapters = [
        "chapter_01_1 网络安全信息.md",
        "chapter_02_2 TIA Portal Openness 自述文件.md",
        "chapter_03_3 TIA Portal Openness 中的新功能.md",
        "chapter_04_4 基本知识.md",
        "chapter_05_5 TIA Portal Openness API.md",
        "chapter_06_6 导出导入.md",
        "chapter_07_7 主要变化.md",
    ]

    for chapter in expected_chapters:
        chapter_path = make_app.srcdir / chapter
        assert chapter_path.exists(), f"章节文件 {chapter} 不存在"


def test_conf_py_exists(make_app):
    """测试 conf.py 存在"""
    conf_path = make_app.confdir / "conf.py"
    assert conf_path.exists(), "conf.py 不存在"


def test_requirements_txt_exists(make_app):
    """测试 requirements.txt 存在"""
    req_path = make_app.confdir / "requirements.txt"
    assert req_path.exists(), "requirements.txt 不存在"


def test_images_dir_exists(make_app):
    """测试 images 目录存在"""
    images_dir = make_app.srcdir / "images"
    assert images_dir.exists(), "images 目录不存在"
    # 检查图片数量
    image_count = len(list(images_dir.glob("*.png")) + list(images_dir.glob("*.jpg")))
    assert image_count > 0, "images 目录中没有图片"
