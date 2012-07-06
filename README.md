<H1 CLASS="western" ALIGN=CENTER>BatchEdit</H1>
<P ALIGN=CENTER STYLE="margin-bottom: 0.14in"><BR><BR>
</P>
<H2 CLASS="western">Introduction:</H2>
<P STYLE="margin-bottom: 0.14in">BatchEdit is a python application
for easily editing photos in batch. It has a simple command-line
interface that will be familiar to UNIX users.</P>
<P STYLE="margin-bottom: 0.14in">BatchEdit has been tested on Windows
7 and Ubuntu Linux. It should work on OSX as well.</P>
<H2 CLASS="western">Prerequisites:</H2>
<UL>
	<LI><P STYLE="margin-bottom: 0.14in">Python 2.7</P>
	<LI><P STYLE="margin-bottom: 0.14in">PIL 1.1.7</P>
</UL>
<H2 CLASS="western">Installation and Usage:</H2>
<OL>
	<LI><P STYLE="margin-bottom: 0.14in">Ensure that the prerequisites
	are met. The application may work with earlier version of Python or
	PIL, but no guarantee.</P>
	<LI><P STYLE="margin-bottom: 0.14in">Copy the BatchEdit.zip file to
	a location of your choice.</P>
	<LI><P STYLE="margin-bottom: 0.14in">From a command prompt, type the
	following:</P>
</OL>
<P STYLE="margin-bottom: 0.14in"><FONT FACE="Consolas, serif"><FONT SIZE=2>python
[path to BatchEdit]\BatchEdit.zip --input [input folder] --output
[output folder] [other options]</FONT></FONT></P>
<OL START=4>
	<LI><P STYLE="margin-bottom: 0.14in">To get a list of all available
	options, type<FONT FACE="Consolas, serif"><FONT SIZE=2> --help.</FONT></FONT></P>
</OL>
<P STYLE="margin-bottom: 0.14in">Note that there is no need to unzip
the &lsquo;BatchEdit.zip&rsquo; file.</P>
<H2 CLASS="western">Command-line Options:</H2>
<P STYLE="margin-bottom: 0.14in">The following command-line options
are available to tweak the settings and specify operations to perform
on all of the images.</P>
<H3 CLASS="western">Settings:</H3>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT FACE="Consolas, serif"><FONT SIZE=2><B>--input
[path]:</B></FONT></FONT> A directory with images to process
(required). If the directory contains spaces, be sure to enclose it
in double quotes.</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT FACE="Consolas, serif"><FONT SIZE=2><B>--output
[path]:</B></FONT></FONT> A directory to output the process images to
(required). The directory must exist. Enclose the directory in double
quotes if needed.</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT FACE="Consolas, serif"><FONT SIZE=2><B>--quality
[value]:</B></FONT></FONT> An integer from 1 - 100 indicating the
quality of the output image. Defaults to 95.</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT FACE="Consolas, serif"><FONT SIZE=2><B>--files
[filters]:</B></FONT></FONT> String representing the UNIX glob
pattern. Supports &lsquo;[ ]&rsquo; character ranges, &lsquo;?&rsquo;
and &lsquo;*&rsquo;. Defaults to '*.jpg'. On Linux, be sure to
enclose the filters in quotes to prevent it from expanding in place.</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT FACE="Consolas, serif"><FONT SIZE=2><B>--forceorder:</B></FONT></FONT>
A flag indicating whether the commands should be executed exactly in
the order typed. Defaults to false.</P>
<H3 CLASS="western">Photo Operations:</H3>
<P STYLE="margin-bottom: 0in; line-height: 100%">Many of the filters
take a decimal argument for the strength. A value of 1 returns the
original image. A value less than 1 will decrease the effect, while a
value greater will increase it. With the exception of <FONT FACE="Consolas, serif"><FONT SIZE=2>--watermark</FONT></FONT>,
all of the arguments are optional.</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT FACE="Consolas, serif"><FONT SIZE=2><B>--sharpen
[strength]:</B></FONT></FONT> Blurs or sharpens the image according
to the strength. Defaults to 1.3.</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT FACE="Consolas, serif"><FONT SIZE=2><B>--contrast
[strength]:</B></FONT></FONT> Decreases or increases contrast based
on the strength provided. Defaults to 1.15.</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT FACE="Consolas, serif"><FONT SIZE=2><B>--brightness
[strength]:</B></FONT></FONT><FONT FACE="Consolas, serif"><FONT SIZE=2>
</FONT></FONT>Decreases or increases brightness based on the strength
provided. Defaults to 1.</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT FACE="Consolas, serif"><FONT SIZE=2><B>--saturation
[strength]:</B></FONT></FONT> Decreases or increases the vibrancy of
the color. Defaults to 1.15.</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT FACE="Consolas, serif"><FONT SIZE=2><B>--grayscale:</B></FONT></FONT>
Converts the image to grayscale.</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT FACE="Consolas, serif"><FONT SIZE=2><B>--autorotate:</B></FONT></FONT>
Reads the exif tags of the image, if available, and attempts to
auto-rotate the image accordingly. When used in conjunction with
<FONT FACE="Consolas, serif"><FONT SIZE=2>--forceorder</FONT></FONT>,
<FONT FACE="Consolas, serif"><FONT SIZE=2>--autorotate</FONT></FONT>
must be the first operation in order to work.</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT FACE="Consolas, serif"><FONT SIZE=2><B>--resize
[longest side]:</B></FONT></FONT> Resizes the longest dimension in
the image to the value specified. Maintains the aspect ratio. When
provided, expects the argument to be an integer. Defaults to 640
pixels. Note that <FONT FACE="Consolas, serif"><FONT SIZE=2><B>--resize</B></FONT></FONT><FONT FACE="Consolas, serif"><FONT SIZE=2>
</FONT></FONT>does not take into account border sizes. For example,
if you resize to 640 pixels and add a border with a thickness of 5,
the resulting image size will be 640 + 5 + 5 = 650 pixels.</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT FACE="Consolas, serif"><FONT SIZE=2><B>--border
[thickness[,color]]:</B></FONT></FONT> Draws a black border with the
thickness and color specified on all sides. The thickness should be a
positive whole number. The color should be a text description, such
as &ldquo;black&rdquo; or &ldquo;red.&rdquo; Defaults to 10 pixels
with a fill of black.</P>
<P STYLE="margin-bottom: 0.14in"><FONT FACE="Consolas, serif"><FONT SIZE=2><B>--watermark
[path to image]:</B></FONT></FONT> Overlays the specified image in
the lower middle as a watermark.  The argument expects a path to the
file to overlay (required). Supports transparency.</P>
<H2 CLASS="western">Order of Operations:</H2>
<P STYLE="margin-bottom: 0.14in">Operations happen in the following
order:</P>
<H3 CLASS="western">First:</H3>
<P STYLE="margin-bottom: 0.14in"><FONT FACE="Consolas, serif"><FONT SIZE=2>--autorotate</FONT></FONT></P>
<H3 CLASS="western">Second:</H3>
<P STYLE="margin-bottom: 0.14in"><FONT FACE="Consolas, serif"><FONT SIZE=2>--contrast<BR>--saturation<BR>--brightness<BR>--grayscale</FONT></FONT></P>
<H3 CLASS="western">Third:</H3>
<P STYLE="margin-bottom: 0.14in"><FONT FACE="Consolas, serif"><FONT SIZE=2>--resize</FONT></FONT></P>
<H3 CLASS="western">Last:</H3>
<P STYLE="margin-bottom: 0.14in"><FONT FACE="Consolas, serif"><FONT SIZE=2>--sharpen<BR>--border<BR>--watermark</FONT></FONT></P>
<P STYLE="margin-bottom: 0.14in">Operations within the same group
will happen in the order typed. To force all operations to happen in
the order typed, regardless of these groupings, use the <FONT FACE="Consolas, serif"><FONT SIZE=2>--forceorder</FONT></FONT>
option.</P>
<H2 CLASS="western">Examples:</H2>
<OL>
	<LI><P STYLE="margin-bottom: 0.14in">We want to auto rotate,
	increase contrast,  convert to grayscale, resize to 720 pixels,
	sharpen, add a gray border of 5 pixels, and overlay a watermark.</P>
</OL>
<P STYLE="margin-bottom: 0.14in"><FONT FACE="Consolas, serif"><FONT SIZE=2>python
scripts\BatchEdit.zip --input C:\input --output C:\output
--autorotate<BR>--resize 720 --grayscale --contrast --sharpen 1.3
--border 5,gray<BR>--watermark C:\logo_transparent.png</FONT></FONT></P>
<P STYLE="margin-bottom: 0.14in">
</P>
<P STYLE="margin-bottom: 0.14in">Note that because we left out the
<FONT FACE="Consolas, serif"><FONT SIZE=2>--contrast</FONT></FONT>
argument, it will default to 1.15.</P>
<OL START=2>
	<LI><P STYLE="margin-bottom: 0.14in">We want to only look for .jpg
	files starting with &ldquo;IMG_&rdquo; in our input folder. We want
	to set the quality to 70. We want to blur the image and add a thick
	red border <I>before</I> resizing.  To prevent the application from
	re-ordering our operations, we will use the <FONT FACE="Consolas, serif"><FONT SIZE=2>--forceorder</FONT></FONT>
	option.</P>
</OL>
<P STYLE="margin-bottom: 0.14in"><FONT FACE="Consolas, serif"><FONT SIZE=2>python
scripts\BatchEdit.zip --input C:\input --output C:\output<BR>--files
&lsquo;IMG_*.jpg&rsquo; --quality 70 --sharpen -5 --border 20,red
--brightness 1.2<BR>--resize --forceorder</FONT></FONT></P>
<P STYLE="margin-bottom: 0.14in">Note that because we left out the
<FONT FACE="Consolas, serif"><FONT SIZE=2>--resize</FONT></FONT>
parameter, it will default to 640 pixels.</P>
