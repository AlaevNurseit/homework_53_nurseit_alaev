def validate_todolist(todolist):
    errors = {}

    if not todolist.description:
        errors['description'] = 'Описание не должно быть пустым!'
    return errors