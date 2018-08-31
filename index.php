
<html>
  <head>
    <title>TrendLink</title>
    <script src="popup.js"></script>
    <style>
    h1{
    color: black;
    }
        tr
        {
            padding: 20px;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.4), 0 6px 20px 0 rgba(0, 0, 0, 0.22);
          }
        table
        {
            border-collapse: separate;
            border-spacing: 20px;
        }
        
        a
        {
            text-decoration: none;
        }
    </style>
  </head>
  <body> 
 <?php
// $json = file_get_contents('/Users/jayantsingh/desktop/data.json');
$json=file_get_contents('http://shreyakhanna06.000webhostapp.com/data.json');
$json_data = json_decode($json,true);
?>
      
<h1><center>Shop Trends</center> </h1>
	
  <table style="width:%;90 height:90%;">
  
    <?php
    for($i=0;$i<sizeof($json_data);$i++)
    {
     
      
   ?>
     
    <tr class="index">
         
    <td><img src="<?php echo $json_data[$i]['image']; ?>" alt="happy me!" width="250" height="250"></td>
    <td><a href="<?php echo $json_data[$i]['url']; ?>" target="_blank"><?php echo $json_data[$i]['name']; ?>"</a></td>
	<td><?php echo $json_data[$i]['discount_price']?></td>
        

	</tr>
      
      
    <?php
    }
    ?>
	<hr>
    </table>
    </body>
    </html>