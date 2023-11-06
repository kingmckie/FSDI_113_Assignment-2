1. Create a new django project in this directory (`~/Code/SDGKU/issue_mgr`)
2. Create the following apps:
2.1. pages
2.2. issues
2.3. accounts
3. Create a model for issues within `issues/models.py` that supports the following fields:
3.1. summary
3.2. description
3.3. reporter (foreign key to user model)
3.4. assignee (foreign key to user model)
3.5. status (foreign key to separate status model)
3.6. created_on (timestamp)



4. Create a separate status model with name and description

## Note
Add the `related_name` attribute to assignee, for example:
```
assignee = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name="assignee"
)