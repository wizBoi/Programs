<!DOCTYPE html>
<head>
    <title>4 PIN MD5 Crack STK</title>
</head>
<body>
    <h1 style="color: #800080;">4 PIN MD5 hash Bruteforcer</h1>
    <h3>
    This application will take the MD5 hash of a 4 digit PIN and attempt to hash all combinations to generate the original sequence.
    </h3>
    <br>
    <form>
        Enter MD5 hash:<input type="text" name="md5" />
        <input type="submit" value="Compute MD5"/>
    </form>
    </br>
    <p>Debug Output: </p>
<pre>
<?php
    $md5= $_GET['md5'];
    $final=0;
    $count=0;
    $time_pre = microtime(true);
    for($i=0; $i<10;$i++)
    {
        for($j=0; $j<10;$j++)
        {
            for($k=0; $k<10;$k++)
            {
                for($l=0; $l<10;$l++)
                {   
                    $tryval=strval($i.$j.$k.$l);
                    $finalHash=hash('md5',$tryval);
                    if ($count<15)
                    {
                        print "$finalHash $tryval \n";
                    }
                    $count=$count+1;

                    if( $finalHash==$md5)
                    {
                        $final=$tryval;
                        $time_post = microtime(true);
                        echo "\nElapsed time: ",$time_post-$time_pre," seconds.\n";
                        break;
                    }
                }
            }
        }
    }

    if($final==0)
    {
        $final=" Invalid input entered.";   /*This output will be generated if value isn't 4 PINs or an Invalid entry altogether. */
    }

?>
</pre>
<br>
<h2>The original PIN is: <?=htmlentities($final)?></h2>

</body>
</html>