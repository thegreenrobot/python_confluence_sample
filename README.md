Purpose
=======
A working example of how to write to a Confluence Wiki using Python and Jinja2 templates.

Overview
========
I needed a method to update Confluence Wiki pages in an automated fashion. In this working example, data is being read from multiple JSON files and sent to a Jinja2 template.  This template is then rendered as content and saved to a page in Confluence.

Libraries
=========
* Jinja2 => http://jinja.pocoo.org/docs/

Usage
=====
* Change the Confluence URL
* Put in a valid Confluence username and password
* Put in the appropriate Confluence space and page name
* The page must exist!  You can update an existing page but not create one
