program = {
    "name": "software engineering",
    "years_of_study": 4,
    "program_structure": {"semesters": []},
}


def create_program_structure(program, **kwargs):
    semesters_per_year = 2

    total_semesters = 0

    if program["years_of_study"]:
        total_semesters = (
            program["years_of_study"] * semesters_per_year
        )  # number of semesters in a year are 2

        # create a semester

        program_semesters = program["program_structure"]["semesters"]

        for semester in range(total_semesters):
            new_term = {}

            new_term["type"] = "semester"
            program_semesters.append(new_term)

        new_recess_term = {}

        for count in range(0, len(program_semesters), 2):
            new_recess_term["type"] = "recess_term"
            print(new_recess_term)
            program_semesters.insert(count + 2, new_recess_term)

    return program


p = create_program_structure(program)

print(p["program_structure"]["semesters"])
