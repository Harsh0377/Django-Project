# Django-Project
### This is the web application that allow user to upload csv file and performs data analysis.
https://github.com/user-attachments/assets/40fbc743-6f9d-48c8-b821-2d959f2c446e
<hr>
<h3>Project Explanation </h3>
<h4>Problem Statement : Create a Django based web application that allows users to upload CSV files, performs data analysis using pandas and numpy, and displays the results and visualization on the web interface.</h4>

<h4>Pre-requisite :</h4>
<ul>
  <li>Familiar with Python programming and Django framework</li>
  <li>Python, Django install on the pc</li>
  <li>Visual Studio or any other IDE install in computer</li>
</ul>  

<hr>

<h4>Steps Involve in Creating the project</h4>
<ol>
  <li>Django Setup</li>
  <li>File Uploading Feature</li>
  <li>Data Preprocessing</li>
  <li>Data Visualization</li>
  <li>User Interface</li>
</ol> 

<hr>

<h4>Brief Explanation of Project</h4>
<p>First we have to create a Django project and Django app within the project. Configure it as per your choice. Then implement a form that allows users to upload "csv files". Perform Data Processing use pandas to read the uploaded csv and perform some basic data analysis task such as Display few rows of the data, Calculating summary statistics operation like mean, median and then identify and handle mising values. Perform Data Visualization like generate plot using seaborn such as Histogram for numerical column and display the plot on web page. Finally create simple and user-friendly interface that display the data analysis result and visualization in organized manner using Django templates. (Note: Above video (Demo.mp4) is the final result we get after doing the project.)</p>

<hr>

<h4>Instruction</h4>
<p>(Note: All the file are stored inside the "v3project.zip" file.)</p>
<ul>
  <li>"Upload.html" file is the user interface visible to user.</li>
  <li>"Result.html" file display output to the user at the end.</li>
  <li>"style.css" file is for styling.</li>
  <li>"forms.py" file to create form</li>
  <li>"urls.py" is the myapp(inside app folder) of the project.</li>
  <li>"views.py" in this we going to perform some operation related to analysis and visualization on dataset.</li>
  <li>"Twitter_posts.csv" is for sample data on which operation is perform.</li>
</ul>
<hr>

<h4>Setup Instruction</h4>
<p>Open cmd and check python and django install in the system.</p>
<p>If install you are ready to go, if not, install python.</p>
<p>After install python type "pip install django" in cmd to install django.</p>
<ol>
  <li>First open vs code in a new window and type "django-admin startproject v3project" in terminal. Here v3project is the project folder name.</li>
  <li>Open the "v3project" folder directory and create project app "myapp" inside it using terminal, run command "python manage.py startapp myapp"</li>
  <li>Make static(for css file), templates(for html file), media(for storing the visual figure) folder inside v3project folder.</li>
  <li>Download the "v3project.zip" file and copy the "results.html", "upload.html" file inside the templates folder, "style.css" into static folder.</li>
  <li>Create a forms.py file to take upload file inside the myapp folder, or copy the code of "forms.py" inside it.</li>
  <li>Link the myapp(make urls.py file inside the folder) to project folder using "urls.py", or copy the code in "v3project/urls.py" and "myapp/urls.py" from zip file that download.</li>
  <li>At last come the logic of visualization, analysis we are going to perform on the data. This all are going to written in "v3project/views.py"</li>
  <li>Copy all the content inside the views.py to the above directory.</li>
  <li>After doing all the above steps run the mange.py file in the terminal "python manage.py runserver"</li>
  <li>Congrats !! There your's website.</li>
  <li>Use sample dataset "Twitter_posts.csv" to run to check the output.</li>
</ol>

