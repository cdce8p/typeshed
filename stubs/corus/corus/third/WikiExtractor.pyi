from _typeshed import Incomplete
from collections.abc import Generator
from math import (
    acos as acos,
    asin as asin,
    atan as atan,
    ceil as ceil,
    cos as cos,
    exp as exp,
    floor as floor,
    pi as pi,
    sin as sin,
    tan as tan,
    trunc as trunc,
)
from typing import TypeVar

PY2: Incomplete
text_type = str
version: str
options: Incomplete
templateKeys: Incomplete
filter_disambig_page_pattern: Incomplete
g_page_total: int
g_page_articl_total: int
g_page_articl_used_total: int

def keepPage(ns, catSet, page): ...
def get_url(uid): ...

selfClosingTags: Incomplete
placeholder_tags: Incomplete

def normalizeTitle(title): ...
def unescape(text): ...

comment: Incomplete
nowiki: Incomplete

def ignoreTag(tag) -> None: ...

selfClosing_tag_patterns: Incomplete
placeholder_tag_patterns: Incomplete
preformatted: Incomplete
externalLink: Incomplete
externalLinkNoAnchor: Incomplete
bold_italic: Incomplete
bold: Incomplete
italic_quote: Incomplete
italic: Incomplete
quote_quote: Incomplete
spaces: Incomplete
dots: Incomplete

_T = TypeVar("_T")

class Template(list[_T]):
    @classmethod
    def parse(cls, body): ...
    def subst(self, params, extractor, depth: int = 0): ...

class TemplateText(text_type):
    def subst(self, params, extractor, depth): ...

class TemplateArg:
    name: Incomplete
    default: Incomplete
    def __init__(self, parameter) -> None: ...
    def subst(self, params, extractor, depth): ...

class Frame:
    title: Incomplete
    args: Incomplete
    prev: Incomplete
    depth: Incomplete
    def __init__(self, title: str = "", args=[], prev: Incomplete | None = None) -> None: ...
    def push(self, title, args): ...
    def pop(self): ...

substWords: str

class Extractor:
    id: Incomplete
    revid: Incomplete
    title: Incomplete
    text: Incomplete
    magicWords: Incomplete
    frame: Incomplete
    recursion_exceeded_1_errs: int
    recursion_exceeded_2_errs: int
    recursion_exceeded_3_errs: int
    template_title_errs: int
    def __init__(self, id, revid, title, lines) -> None: ...
    def write_output(self, out, text) -> None: ...
    def extract(self, out) -> None: ...
    def transform(self, wikitext): ...
    def transform1(self, text): ...
    def wiki2text(self, text): ...
    def clean(self, text): ...
    maxTemplateRecursionLevels: int
    maxParameterRecursionLevels: int
    reOpen: Incomplete
    def expand(self, wikitext): ...
    def templateParams(self, parameters): ...
    def expandTemplate(self, body): ...

def splitParts(paramsList): ...
def findMatchingBraces(text, ldelim: int = 0) -> Generator[Incomplete]: ...
def findBalanced(text, openDelim=["[["], closeDelim=["]]"]) -> Generator[Incomplete]: ...
def if_empty(*rest): ...
def functionParams(args, vars): ...
def string_sub(args): ...
def string_sublength(args): ...
def string_len(args): ...
def string_find(args): ...
def string_pos(args): ...
def string_replace(args): ...
def string_rep(args): ...
def roman_main(args): ...

modules: Incomplete

class MagicWords:
    names: Incomplete
    values: Incomplete
    def __init__(self) -> None: ...
    def __getitem__(self, name): ...
    def __setitem__(self, name, value) -> None: ...
    switches: Incomplete

magicWordsRE: Incomplete

def ucfirst(string): ...
def lcfirst(string): ...
def fullyQualifiedTemplateTitle(templateTitle): ...
def normalizeNamespace(ns): ...

class Infix:
    function: Incomplete
    def __init__(self, function) -> None: ...
    def __ror__(self, other): ...
    def __or__(self, other): ...
    def __rlshift__(self, other): ...
    def __rshift__(self, other): ...
    def __call__(self, value1, value2): ...

ROUND: Incomplete

def sharp_expr(extr, expr): ...
def sharp_if(extr, testValue, valueIfTrue, valueIfFalse: Incomplete | None = None, *args): ...
def sharp_ifeq(extr, lvalue, rvalue, valueIfTrue, valueIfFalse: Incomplete | None = None, *args): ...
def sharp_iferror(extr, test, then: str = "", Else: Incomplete | None = None, *args): ...
def sharp_switch(extr, primary, *params): ...
def sharp_invoke(module, function, args): ...

parserFunctions: Incomplete

def callParserFunction(functionName, args, extractor): ...

reNoinclude: Incomplete
reIncludeonly: Incomplete

def define_template(title, page) -> None: ...
def dropNested(text, openDelim, closeDelim): ...
def dropSpans(spans, text): ...
def replaceInternalLinks(text): ...
def makeInternalLink(title, label): ...

wgUrlProtocols: Incomplete
EXT_LINK_URL_CLASS: str
ANCHOR_CLASS: str
ExtLinkBracketedRegex: Incomplete
EXT_IMAGE_REGEX: Incomplete

def replaceExternalLinks(text): ...
def makeExternalLink(url, anchor): ...
def makeExternalImage(url, alt: str = ""): ...

tailRE: Incomplete
syntaxhighlight: Incomplete
section: Incomplete
listOpen: Incomplete
listClose: Incomplete
listItem: Incomplete

def compact(text): ...
def handle_unicode(entity): ...

class NextFile:
    filesPerDir: int
    path_name: Incomplete
    dir_index: int
    file_index: int
    def __init__(self, path_name) -> None: ...
    def __next__(self): ...
    next = __next__

class OutputSplitter:
    nextFile: Incomplete
    compress: Incomplete
    max_file_size: Incomplete
    file: Incomplete
    def __init__(self, nextFile, max_file_size: int = 0, compress: bool = True) -> None: ...
    def reserve(self, size) -> None: ...
    def write(self, data) -> None: ...
    def close(self) -> None: ...
    def open(self, filename): ...

tagRE: Incomplete
keyRE: Incomplete
catRE: Incomplete

def load_templates(file, output_file: Incomplete | None = None) -> None: ...
def pages_from(input) -> Generator[Incomplete]: ...
def process_dump(input_file, template_file, out_file, file_size, file_compress, process_count) -> None: ...
def extract_process(opts, i, jobs_queue, output_queue) -> None: ...

report_period: int

def reduce_process(
    opts, output_queue, spool_length, out_file: Incomplete | None = None, file_size: int = 0, file_compress: bool = True
) -> None: ...

minFileSize: Incomplete

def main() -> None: ...
def createLogger(quiet, debug, log_file) -> None: ...
