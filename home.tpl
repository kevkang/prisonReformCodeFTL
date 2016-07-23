<!DOCTYPE html>
<html lang="en">
  <head>

  </head>
  <body>
    <meta charset="utf-8">
    <div>
	    <form method="POST"> 
	    	Contact Email: <input type="text" name="email"><br>
	    	Company Name:<input type="text" name="compName"> <br>
	    	Job Title:<input type="text" name="jobTitle"> <br>
	    	Skills Required:<input type="text" name="skillReq"> <br>
	    	Upload training material:<input type="file" name="trainingMaterial"> <br>
	    	Openings:<input type="text" name="openings"> <br>
	    	Budget:<input type="text" name="budget"> <br>
	    	Number of Positions needed:<input type="text" name="numPos"> <br>
	    	Wait time:<input type="text" name="waitTime"> <br>
	    	<input type="submit" value = "Submit"></button>
	    	<!--submit-->
		</form>
	</div>
	<div>
	<!--calculates benefit-->
		<table>
			<tr>
				<td> Projected hourly wage</td>
				<td> $<input type="number" id="hourlyWage" onchange="calcTaxCredit();" min="0" /> </td>
			</tr>
			<tr>
				<td> Projected # of hours worked </td>
				<td> &nbsp;<input type="number" id="hoursWorked" onchange="calcTaxCredit();" min="0"  /> </td>
			</tr>
			<tr>
				<td> Tax credit for hiring the individual </td>
				<td> $<input type="text" disabled id="taxCredit" /> </td> 
			</tr>
		</table>
	</div>
	  <script>
	function calcTaxCredit(){
		var hoursWorked = document.getElementById("hoursWorked").value;
		var hourlyWage = document.getElementById("hourlyWage").value;
		var taxCredit = document.getElementById("taxCredit")
		var total = hourlyWage * hoursWorked;
		// tax credit limit $2400
		// not eligible if less than 120 projected hours worked
		if (hoursWorked < 120)
		{
			taxCredit.value = "0";
		} else if (hoursWorked < 400) {
			if (total * 0.25 > 2400) { // apply 25% tax credit rate if hours worked between 120 and 400
				taxCredit.value = "2400";
			} else {
				taxCredit.value = total * 0.25;
			}
		} else {
			if (total * 0.4 > 2400) { // apply 40% tax credit rate if hours worked 400 or more
				taxCredit.value = "2400";
			} else {
				taxCredit.value = total * 0.4;
			}
		}
	}
</script>
    </body>
    </html>
