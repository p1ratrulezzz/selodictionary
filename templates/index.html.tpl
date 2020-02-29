<!doctype html>
<html lang="ru">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>${page['title']}</title>

    <meta name="description" content="Словарь с неординарными фразами, о которых мало кто слышал. Узнай новые слова и выпендрись перед тянками!">
    <meta name="keywords" content="словарь, сельский словарь, модные слова, современный словарь, современные слова, интересные слова${page['keywords']}">
    <meta name="robots" content="index, follow">
    <meta name="language" content="RU">
    <meta name="author" content="P1ratRuleZZZ">
    <meta name="distribution" content="global">
    <meta name="rating" content="mature">
    <meta name="generator" content="FreeMetaTagGenerator.com">
</head>
<body>
<div class="main-wrapper container">
    <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <a class="navbar-brand" href="#"><a href="/"><h1>${page['title']}</h1></a></a>
        </div>
    </div>
    <div class="row row-cols-2">
        <div class="col-sm col-sm-1">
            <nav id="glossary-navigation" class="navbar navbar-fixed-left sticky-top">
                <nav class="nav navbar-glossary">
                    % for key in page['dictionary']:
                    <% item = page['dictionary'][key] %>
                        <a class="nav-link" href="#glossary-index-${item['index']}">${item['letter']}</a>
                    % endfor
                </nav>
            </nav>
        </div>
        <div class="col-sm" data-spy="scroll" data-offset="0" data-target="#glossary-navigation">

            % for key in page['dictionary']:
                <% item = page['dictionary'][key] %>
                <h4 id="glossary-index-${item['index']}"></h4>
                % for word in item['words']:
                    ${word}
                % endfor
            % endfor

            <div class="footer-wrapper">
                <a href="https://github.com/p1ratrulezzz/selodictionary/blob/master/README.md">Добавить еще слов в сельский словарь</a>
            </div>
        </div>
    </div>
</div>

<!-- Optional JavaScript -->
<!-- jQuery first, then Popper.js, then Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</body>
</html>