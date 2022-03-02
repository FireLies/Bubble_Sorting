
function Bubble () {

    $Arr = @()
    $Elements = 50

    for ($i = 0; $i -lt $Elements; $i++) {
        $Arr += (Get-Random -Maximum 25 -Minimum 1)
    }

    $Unsorted = Write-Output ($Arr -join ', ')

    for ($i = 0; $i -lt ($Arr.Length); $i++) {
        for ($j = 0; $j -lt ($Arr.Length - $i - 1); $j++) {
          
            if ($Arr[$j] -gt $Arr[$j + 1]) {
                $Arr[$j], $Arr[$j + 1] = $Arr[$j + 1], $Arr[$j]

                Clear-Host

                $Unsorted

                ""
                Write-Host ($Arr -join ', ') `n -ForegroundColor 'Cyan'
                Start-Sleep -Milliseconds 1
            }
        }
    }
}

Bubble