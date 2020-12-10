c = get_config()
c.Exporter.preprocessors = [
    "bibpreprocessor_html.BibTexPreprocessor",
    "pre_pymarkdown.PyMarkdownPreprocessor",
]


c.LatexExporter.template_file = "./revtex_nocode.tplx"

c.TemplateExporter.exclude_input = True
