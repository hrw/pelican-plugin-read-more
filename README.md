# What is it?

My blog was WordPress based for many years. One of functionalities I used was
ability to split post into 'entry' and 'rest' by adding "\<!--MORE-->" into
content.

This plugin adds such functionality into Pelican.

# Usage

Install, add "\<!--MORE-->" into post content and then index will get only part
before that marker.

The "Read more&hellip;" text is inside of paragraph with 'readmore' class. My
CSS for it:

```css

.readmore {
	text-align: right;
}

.readmore a {
	font-weight: bold;
}
```
