from flask import flash


def flash_errors(form, category) -> None:
    for field, errors in form.errors.items():
        for error in errors:
            # sometimes you have to handle non-field errors:
            # for example, "invalid username or password"
            if field is None:
                flash(f"{error}", category)
            else:
                flash(f"{field}: {error}", "error")
