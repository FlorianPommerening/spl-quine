from . import prefixsection, datasection, codesection


def generate(filename):
    prefix = prefixsection.generate()
    code = codesection.generate(prefix)
    data = datasection.generate(code)
    with open(filename, "w") as outfile:
        outfile.write(prefix)
        outfile.write(data)
        outfile.write(code)

