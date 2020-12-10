
#当日日付を定義
dn = Time.now
dt = dn.strftime("%Y%m%d_%H%M%S") 

filename = dt + ".txt"
dirname = dt
puts filename
puts dirname

#ディレクトリの新規作成
Dir.mkdir(dirname)

#ファイルの新規作成
newfile = File,open("#{dirname}/#{filename}","w")
newfile.push()

print "=== Processing completed ==="