<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <div>
	    <form method="POST"> 
	    	Contact Email: <input type="text" name="email"><br>
	    	Company Name:<input type="text" name="compName"> <br>
	    	Job Title:<input type="text" name="jobTitle"> <br>
	    	Skills Required:<input type="text" name="skillReq"> <br>
	    	Upload training material:<input type="file" name="trainingMaterial"> <br>
	    	Budget:<input type="text" name="budget"> <br>
	    	Number of Positions needed:<input type="text" name="numPos"> <br>
	    	Wait time:<input type="text" name="waitTime"> <br>
	    	<input type="submit" value = "Submit"></button>
	    	<!--submit-->
		</form>
	</div>
	<div>
	<!--calculates benefit-->
		<div>Your Benefit : {{benefit}}</div>
	</div>
    </head>
    </html>
