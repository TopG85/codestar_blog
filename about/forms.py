from collab.forms import CollaborateForm

# Re-export CollaborateForm from the collab app so the About page can
# import the form from `about.forms` without duplicating model logic.
__all__ = ["CollaborateForm"]
