	function createTable()
	{
		var num_rows = document.getElementById('rows').value;
		var num_cols = document.getElementById('cols').value;
		var theader = '<table class = "table table-bordered table-responsive"> <thead><input placeholder="title" name = "title"/> </thead>\n';
		theader += '<tr> <th scope="col">Criteria</th>';
		for(var i =0; i<=num_cols-2;i++){
			theader += `<th scope="col"><input type="text" value = ${i+1} name = "head${i+1}" ></input></th>`;
		}
		theader += "</tr>";
		var tbody = '';

		for( var i=0; i<num_rows;i++)
		{
			tbody += '<tr>';
			for( var j=0; j<num_cols;j++)
			{
				tbody += `<td contenteditable> <input type = "text" id= "category" name = ${i}${j}  >`;

				tbody += '</td>'
			}
			tbody += '</tr>\n';
		}
		var tfooter = '</table>';
		document.getElementById('rubricframe').innerHTML = theader + tbody + tfooter;
	}