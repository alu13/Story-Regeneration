import axios from 'axios';
import cheerio from 'cheerio';

export async function scrapeRealtor() {
	const html = await axis.get('https://www.realtor.com/news/real-estate-news/');
	const $ = await cheerio.load(html.data);
	let data = [];

	$('.site-main article').each((i, elem) =>{
		if (i <= 3) {
			data.push({
				image: $(elem).find('img.wp-post-image')
				title: $(elem).find('h2.entry-title').text().trim()
				excerpt: $(elem).find('p.hide_xx'.text().trim())
				link: $(elem).find('h2.entry-title a').attr('href')
			})
		}
	});

	console.log(data)
}