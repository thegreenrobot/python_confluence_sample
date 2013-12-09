Purpose
=======
A working example of how to write to a Confluence Wiki using Python and Jinja2 templates.

Overview
========
I needed a method to update Confluence Wiki pages in an automated fashion. In this working example, data is being read from multiple JSON files and sent to a Jinja2 template.  This template is then rendered as content and saved to a page in Confluence.

Libraries
=========
I chose to use Jinja2 for templating the html that needs to be saved to the Confluence page as it eliminates having to write out all of the html in python (much prettier).
* Jinja2 => http://jinja.pocoo.org/docs/

Usage
=====
* Clone the repo
* Create a virtual environment and activate it
* Install the library dependencies (pip install -r requirements.txt)
* Change the Confluence URL
* Put in a valid Confluence username and password
* Put in the appropriate Confluence space and page name


Warning
=======
* The Confluence page must already exist (a blank page is fine)
* You can update an existing page but not create one
