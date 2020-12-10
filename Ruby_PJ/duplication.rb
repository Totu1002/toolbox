require "fileutils"

puts(<<"EOS")
====== Information ======
このプログラムは
以下のフォルダより
対象ファイルを選択し、
指定の個数分、
ファイルをコピーします。
※実行するにはフォルダを作成してください。

実行元フォルダ：
"src_dir"

実行先フォルダ：
"dst_dir"
EOS

src_path = "src_dir"
dst_path = "../dst_dir"

puts "====== ファイル一覧 ======"
Dir.chdir("#{src_path}")
puts "現在Path : "
puts "#{Dir.pwd}"
puts "#{Dir.glob("*.*")}"
puts "========================="


while TRUE do
    puts "対象のファイルを入力してください："
    src_file = gets.chomp
    #src_file = "test1.txt"
    if File.exist?(src_file)
        break
    else
        puts "=== ERROR : ファイルが存在しません ==="
    end
end

#ここのチェック、機能していない
while TRUE do
    puts "生成する個数を入力してください: "
    exe_num = gets.to_i
    #exe_num = 5
    if exe_num.is_a?(Integer)
        range = Range.new(1,exe_num)
        count = 1
        break
    else
        puts "=== ERROR : 数値を入力してください ==="
    end
end

'''
puts "*** test code puts ***"
puts "exe_num.is_a?(Integer) : #{exe_num.is_a?(Integer)}"
puts "exe_num : #{exe_num}"
puts "range : #{range}"
puts "count : #{count}"
puts "**********************"
'''

while TRUE 
    puts "ファイルの名前を変更しますか:[y/n]"
    answer = gets.chomp
    case answer
    when "y"
        puts "新しいファイル名を入力してください:"
        new_name = gets.chomp + File.extname(src_file)
        break
    when "n"
        new_name = File.basename(src_file)
        break
    else
        puts "=== ERROR : 再度入力してください ==="
    end
end

for count in range
    dst_name = "#{count.to_s}_#{new_name}"
    puts dst_name
    FileUtils.cp("#{src_file}","#{dst_path}/#{dst_name}")
    count +=1
end

puts "========================="
puts "======== success ========"
puts "========================="