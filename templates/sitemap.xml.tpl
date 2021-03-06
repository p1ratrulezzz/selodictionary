<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>${url}/</loc>
        <lastmod>${modified}</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.5</priority>
    </url>
    % for word in words:
    <url>
        <loc>${url}/${word['uri']}</loc>
        <lastmod>${word['modified_sitemap']}</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.8</priority>
    </url>
    % endfor
</urlset>
