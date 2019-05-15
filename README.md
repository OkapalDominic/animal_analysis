# Animal-Analysis

Allows the vistor to the site to upload an image and write how they feel about it.
When submit button is pressed, displays the image along with whether they like it.
If the visitor likes what's in the image, then more information will be obtained and displayed.

## Running the app

This was originally deployed to google cloud for my school project.
It is now updated to run locally.

1. [Clone this repo][repo]: https://github.com/OkapalDominic/animal_analysis.git
2. [Tutorial to get flask setup in VS Code][tut], Follow the [Prerequisites][tutPre] and [Create a project environment for the Flask tutorial][tutCreate].  But you can stop before [Create and run a minimal Flask app][tutRun].
2. [Read this][setupAPIkey] to create an api key for cloud services, and download the json to set GOOGLE_APPLICATION_CREDENTIALS.
3. Create a file called .api_key and paste key on the Credentials tab of APIs & Services.
4. Install google cloud libraries: pip install google-cloud-storage
   1. pip install --upgrade google-cloud-vision
   2. pip install --upgrade google-cloud-language
   3. pip install --upgrade google-cloud-translate
5. flask run

[tut]: https://code.visualstudio.com/docs/python/tutorial-flask
[tutPre]: https://code.visualstudio.com/docs/python/tutorial-flask#_prerequisites
[tutCreate]: https://code.visualstudio.com/docs/python/tutorial-flask#_create-a-project-environment-for-the-flask-tutorial
[tutRun]: https://code.visualstudio.com/docs/python/tutorial-flask#_create-and-run-a-minimal-flask-app
[repo]: https://github.com/OkapalDominic/animal_analysis.git
[setupAPIkey]: https://cloud.google.com/docs/authentication/getting-started