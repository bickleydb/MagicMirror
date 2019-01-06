

$startingDirectory = $pwd

$projectPath = "$home\Git\MagicMirror\Javascript"
tsc -p $projectPath

$bundlerPath = "$projectPath\bundler\WindowsConfig"
$configFileList = Get-ChildItem -Path $bundlerPath "*.webpack.config.js"

cd $bundlerPath

For($fileIndex = 0; $fileIndex -le $configFileList.Length; $fileIndex++) {
    $currentFile = $configFileList | Select-Object -Index $fileIndex
    If($currentFile.Name.Length -eq 0) {
        continue
    }
    webpack --config "$bundlerPath\WindowsConfig\$currentFile"
}

cd $startingDirectory