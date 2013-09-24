## Features

NBConvert is distributed with 2 output templates and 4 cell styles.  All 4 cell styles can be used by creating a custom template.  Custom cell styles are also supported.  The implementation of a custom cell style depends on the design requirements.  Here are two possible scenarios, the first being the most flexible:

1.  **A custom cell style that will be used with multiple output templates, possibly including custom output templates**
    This scenario requires two template files.  The first template file is the cell style itself.  The second template file is a custom template that chooses which cell style and output template to use.
    
2.  **A custom cell style that will only be used with one output template**
    This scenario only requires you to create one template file.  It can be implemented by 
        1. writting a *custom template* 
        2. that *sets the cell_style Jinja variable to latex_base.tplx*
           For example: `((* set cell_style = 'style_bw_ipython.tplx' *))`
        3. and then *inherits from the correct output template* (IT'S IMPORTANT THAT THIS IS DONE AFTER STEP 2 BECAUSE OF THE ORDER IN WHICH JINJA EVALUATES THE TEMPLATES!).
        4. Then add all the custom style logic to the custom template.
    The last step causes Jinja to forgoe the built in cell styles.  All the custom cell style logic would then be implemented in the *custom template*

Examples of both can be found in the subdirectories of this directory.