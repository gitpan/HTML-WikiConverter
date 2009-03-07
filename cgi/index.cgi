#!/usr/bin/perl
use warnings;
use strict;

use HTML::WikiConverter::WebApp;

my %config = (
  template_path => '/Users/diberri/Sites/cgi-bin/html2wiki/templates/',
);

HTML::WikiConverter::WebApp->new( PARAMS => \%config )->run;
