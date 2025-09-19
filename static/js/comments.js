const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");
const deleteForm = document.getElementById("deleteForm");

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    // set the form action to the delete URL for this comment
    if (deleteForm) {
      deleteForm.setAttribute('action', `delete_comment/${commentId}`);
    }
    deleteModal.show();
  });
}

// Intercept the delete form submit to use AJAX
if (deleteForm) {
  deleteForm.addEventListener('submit', function (e) {
    e.preventDefault();
    const url = deleteForm.getAttribute('action');
    // send POST via fetch with CSRF token
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
        'X-Requested-With': 'XMLHttpRequest',
      },
      body: JSON.stringify({}),
    })
      .then((resp) => resp.json())
      .then((data) => {
        if (data.success) {
          // reload the page to reflect deletion
          window.location.reload();
        } else {
          // show an alert with the error
          alert(data.error || 'Unable to delete comment');
        }
      })
      .catch((err) => {
        console.error('Delete failed', err);
        // fallback to normal submit
        deleteForm.submit();
      });
  });
}
