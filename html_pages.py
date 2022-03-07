def Success():
    return """<html>
                <head>
                    <link href="https://fonts.googleapis.com/css?family=Nunito+Sans:400,400i,700,900&display=swap" rel="stylesheet">
                </head>
                    <style>
                    body {
                        text-align: center;
                        padding: 40px 0;
                        background: #EBF0F5;
                    }
                        h1 {
                        color: #88B04B;
                        font-family: "Nunito Sans", "Helvetica Neue", sans-serif;
                        font-weight: 900;
                        font-size: 40px;
                        margin-bottom: 10px;
                        }
                        p {
                        color: #404F5E;
                        font-family: "Nunito Sans", "Helvetica Neue", sans-serif;
                        font-size:20px;
                        margin: 0;
                        }
                    i {
                        color: #9ABC66;
                        font-size: 100px;
                        line-height: 200px;
                        margin-left:-15px;
                    }
                    .card {
                        background: white;
                        padding: 60px;
                        border-radius: 4px;
                        box-shadow: 0 2px 3px #C8D0D8;
                        display: inline-block;
                        margin: 0 auto;
                    }
                    </style>
                    <body>
                    <div class="card">
                    <div style="border-radius:200px; height:200px; width:200px; background: #F8FAF5; margin:0 auto;">
                        <i class="checkmark">✓</i>
                    </div>
                        <h1>Success</h1> 
                        <p>We received your purchase request;<br/> we'll be in touch shortly!</p>
                    </div>
                    </body>
                </html>"""

def Failure():
    return """
    
<html>
<head>
<title>CodePen - Simple 404 Page</title>
<style>
*{
    transition: all 0.6s;
}

html {
    height: 100%;
}

body{
    font-family: 'Lato', sans-serif;
    color: #888;
    margin: 0;
    background: #EBF0F5;
}

#main{
    display: table;
    width: 100%;
    height: 100vh;
    text-align: center;
}

.fof{
	  display: table-cell;
	  vertical-align: middle;
}

.fof h1{
	  font-size: 50px;
	  display: inline-block;
	  padding-right: 12px;
	  animation: type .5s alternate infinite;
}

@keyframes type{
	  from{box-shadow: inset -3px 0px 0px #888;}
	  to{box-shadow: inset -3px 0px 0px transparent;}
}

</style>
</head>
<body>
<div id="main">
    	<div class="fof">
        		<h1>Az asztal nem található</h1>
    	</div>
</div>
</body>
<html>"""