from . import prefixsection, datasection, codesection


def generate():
    prefix = prefixsection.generate()
    code = codesection.generate(prefix)
    data = datasection.generate(code)
    return prefix + data + code
