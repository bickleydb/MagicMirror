

$startingDirectory = $pwd

$projectPath = "$home\Git\MagicMirror\Javascript"
tsc -p $projectPath

$configFilePath = "$projectPath\bundler\DevConfig\"
$bundlerPath = "$projectPath\bundler\"

$configFileList = Get-ChildItem -Path $configFilePath "*.webpack.config.js"

cd $bundlerPath

For($fileIndex = 0; $fileIndex -le $configFileList.Length; $fileIndex++) {
    $currentFile = $configFileList | Select-Object -Index $fileIndex
    If($currentFile.Name.Length -eq 0) {
        continue
    }

    webpack --config "$configFilePath\$currentFile"
}

cd $startingDirectory