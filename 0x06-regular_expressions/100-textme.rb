#!/usr/bin/env ruby
SENDER = ARGV[0].scan(/\[from:(.*?)\]/)
RECEIVER = ARGV[0].scan(/\[to:(.*?)\]/)
FLAG = ARGV[0].scan(/\[flags:(.*?)\]/)
puts [SENDER, RECEIVER, FLAG].join(',')
