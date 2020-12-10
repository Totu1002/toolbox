require "pdf-reader"

#PDFファイルから文字列を抽出するプログラム

puts "Please enter the target file name："
target = gets.chomp
#path = "/Users/totu/work/develop/Ruby_PJ/test_tools/"
src_path = "src_dir/"
dst_path = "dst_dir/"
target_file = src_path + target


reader = PDF::Reader.new(target_file)
page_arrays = []

reader.pages.each do |page|
    #puts page.text
    page_arrays.push(page.text)
end

dn = Time.now
dt = dn.strftime("%Y%m%d_%H%M%S") 
filename = "PDFreadText_" + dt + ".txt"
puts "filename is : #{filename}"

File.open(dst_path + filename, "w") do |f|
    f.puts(page_arrays)
end

puts "=== Processing was successful ==="