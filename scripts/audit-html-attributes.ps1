$attributePattern = [regex]'([:\w-]+)\s*='
$tagPattern = [regex]'<[a-zA-Z][\w:-]*(?:\s+[\w:-]+(?:\s*=\s*(?:"[^"]*"|''[^'']*''|[^\s"''=<>`]+))?)*\s*/?>'
$errors = @()

Get-ChildItem -File -Filter '*.html' | ForEach-Object {
    $path = $_.FullName
    $content = Get-Content -Raw -LiteralPath $path

    foreach ($tagMatch in $tagPattern.Matches($content)) {
        $tag = $tagMatch.Value
        $attributeText = [regex]::Replace($tag, '"[^"]*"|''[^'']*''', '""')
        $attributes = @($attributePattern.Matches($attributeText) | ForEach-Object {
            $_.Groups[1].Value.ToLowerInvariant()
        })
        $duplicates = @($attributes | Group-Object | Where-Object { $_.Count -gt 1 } | Select-Object -ExpandProperty Name)

        if ($duplicates.Count -gt 0) {
            $errors += [pscustomobject]@{
                File = $_.Name
                Tag = $tag.Substring(0, [Math]::Min(200, $tag.Length))
                Duplicates = $duplicates -join ', '
            }
        }
    }
}

if ($errors.Count -gt 0) {
    $errors | Format-Table -Wrap -AutoSize
    exit 1
}

Write-Output 'PASS: keine doppelten HTML-Attribute'