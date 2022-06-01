import os


def add_text(
    gitlabPage_name,
    section_title,
    resdir,
    prev_text="",
    ffilter=None,
    extension=".tex",
    startswith_filter=None,
):
    text = f"## {section_title}\r\n"
    pdf_names = []
    for root, dirs, files in os.walk(resdir, topdown=False):
        for f in files:
            if f.endswith(extension) and not f.startswith("_"):
                pdf_names.append(f[: -len(extension)] + ".pdf")
    if ffilter is not None:
        pdfs = sorted(set.intersection(set(ffilter), set(pdf_names)))
    else:
        pdfs = pdf_names

    for files in pdfs:
        if startswith_filter is not None:
            if files.startswith(startswith_filter):
                text += f"- [{files}]({gitlabPage_name}/{files})\r\n"
        else:
            text += f"- [{files}]({gitlabPage_name}/{files})\r\n"

    return prev_text + text

def main():
    with open("doc/head.md", "r") as f:
        head = f.read()

    gitlabPage_name = "https://celmo.gitlab.io/harris/"


    # Add thesis
    text = add_text(
        gitlabPage_name,
        section_title="Thesis",
        resdir="./thesis/thesis/fichiers_latex/Manuscrit/",
        prev_text="",
        ffilter=["Manuscrit.pdf"],
        extension=".tex",
    )

    # Add notes
    text = add_text(
        gitlabPage_name,
        section_title="Notes",
        resdir="./notes/",
        prev_text=text,
        ffilter=["notes.pdf"],
        extension=".tex",
    )

    #  Add reports
    text = add_text(
        gitlabPage_name,
        section_title="Reports",
        resdir="./reports/reu_hcl/",
        prev_text=text,
        extension=".tex",
    )

    text = add_text(
        gitlabPage_name,
        section_title="Anatomy laboratory",
        resdir="./reports/anatomy_laboratory/",
        prev_text=text,
        extension=".tex",
    )

    #  Add presentations
    text = add_text(
        gitlabPage_name,
        section_title="Presentations",
        resdir="./presentations/seminar_symme/",
        prev_text=text,
        startswith_filter="PRES",
        extension=".tex",
    )

    #  Add articles realses
    text = add_text(
        gitlabPage_name,
        section_title="Articles releases",
        resdir="./article/",
        prev_text=text,
        extension=".tex",
    )

    # Add abstracts

    text = add_text(
        gitlabPage_name,
        section_title="Abstracts",
        resdir="./abstract/",
        prev_text=text,
        extension=".tex",
    )


    with open("README.md", "w") as f:
        f.write(text)

    print("Links updates !")
