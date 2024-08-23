from urllib.parse import quote
import ipywidgets as widgets

def generate_notebook_link(notebook_path, canvas_id):
    """
    Generates a URL for accessing a Jupyter Notebook via a custom link.

    Parameters:
    - notebook_path (str): The path to the Jupyter Notebook file.

    Returns:
    - str: An HTML string containing the notebook link.
    """
    # Course parameters
    course_id = "cs1302_24a"
    
    # Base URLs
    notebook_repo = f"https://github.com/dive4dec/{course_id}"
    course_server = "https://dive.cs.cityu.edu.hk"
    course_homepage = f"https://canvas.cityu.edu.hk/courses/{canvas_id}"
    
    # Notebook URL generation
    # 1. Construct the URL for git-pull service to clone or pull the notebook repository
    gitpull_url = (
        f"{course_server}/{course_id}/hub/user-redirect/git-pull?"
        + f"repo={quote(notebook_repo)}"
        + f"&urlpath={quote(f'lab/tree/{course_id}/{notebook_path}')}"
    )
    # Construct the LTI (Learning Tools Interoperability) launch URL for JupyterHub
    lti_url = (
        f"{course_server}/{course_id}/hub/lti/launch?" + f"custom_next={quote(gitpull_url)}"
    )
    # Construct the LTI external tool URL to open the notebook
    notebook_url = (
        f"{course_homepage}/external_tools/retrieve?display=borderless&"
        + f"url={quote(lti_url)}"
    )

    # Split the input string by '/'
    parts = notebook_path.split('/')
    
    # Extract the lecture part and content part
    title = parts[0]
    subtitle = parts[1].rsplit('.', 1)[0].replace('_', ' ')

    html = f"""
<h4>{title}</h4>
<ul>
  <li>
    <a href="{notebook_url}" target=_blank>{subtitle}</a>
  </li>
</ul>
"""
    return html

def setup_notebook_link_widget(canvas_id):
    """
    Sets up and returns a widget for generating and displaying a notebook link.

    The widget consists of a text input for the notebook path and an HTML output
    displaying the generated link. The link updates automatically as the input changes.

    Returns:
    - widgets.VBox: A vertical box widget containing the text input and HTML output.
    """
    # Create a Text widget for input with initial value and description
    text_input = widgets.Text(
        value='Lab0/Course_Materials.ipynb',
        description='Notebook path:',
        disabled=False,
        style={'description_width': 'initial'},  # Increase the description length
        layout=widgets.Layout(width='90%')  # Set the width of the text input
    )

    # Create an HTML widget for displaying the generated link
    html_output = widgets.HTML(
        value=generate_notebook_link(text_input.value, canvas_id=canvas_id)  # Generate initial link
    )

    # Define a callback function to update the HTML widget upon text input changes
    def update_html(change):
        # Update the HTML widget with the new generated link
        html_output.value = generate_notebook_link(change['new'], canvas_id=canvas_id)

    # Attach the callback function to the Text widget to listen for 'value' changes
    text_input.observe(update_html, names='value')

    # Display the widgets in a vertical box layout
    return widgets.VBox([text_input, html_output])