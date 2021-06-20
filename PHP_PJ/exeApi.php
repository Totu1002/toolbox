<?php 
//TODO Nextcloud APIテストコード各種作成→Githubへpush
//メソッド名：スネークケース

class ExeApi {
  private $user;
  private $pass;
  private $url;
  private $api;
  private $api_del_folder;
  
//検証環境用パラメータ
  public function __construct()
  {
    $this->user = "admin";
    $this->pass = "admin";
    $this->url = 'http://admin:admin@192.168.33.10/nextcloud/';
    $this->api = 'remote.php/dav/files/admin/';
  }

  public function run () {
    //foreachで自動複数生成する
    $folder = 'API_test_folder';
    //$folder_array = array('API_test_folder');

    //以下のメソッドは自動生成されたフォルダを対象に動作する
    //対象をしてする場合はここで別途定義する
    //$folder = '';

    //$this->make_folder($folder);
    //$this->upload_files($folder);
    
    $this->get_info($folder);
  
  }

  
  //フォルダ作成
  public function make_folder($folder){
    $user = $this->user;
    $pass = $this->pass;
    $url = $this->url;
    $api = $this->api;
    
    $ch = curl_init();
    curl_setopt_array($ch,[
      CURLOPT_CUSTOMREQUEST => 'MKCOL',
      //CURLOPT_URL => $url . $api . pathinfo($folder),
      CURLOPT_URL => $url . $api . $folder,
      CURLOPT_USERPWD => $user . ':' . $pass,
      CURLOPT_RETURNTRANSFER => 'TRUE',
      CURLOPT_FOLLOWLOCATION => 'TRUE',
      CURLOPT_SSL_VERIFYPEER => 'FALSE',
    ]);
    curl_exec($ch);
    curl_close($ch);
  }

  //ファイルアップロード
  public function upload_files($folder){
    $user = $this->user;
    $pass = $this->pass;
    $url = $this->url;
    $api = $this->api;
    //アップロードをするファイルを一括取得
    $put_files = glob("");

    foreach($put_files as $put_file){
      $ch = curl_init();
      curl_setopt_array($ch,[
        CURLOPT_CUSTOMREQUEST => 'PUT',
        CURLOPT_URL => $url . $api . '/' . $folder . pathinfo($put_file),
        CURLOPT_USERPWD => $user . ':' . $pass,
        CURLOPT_RETURNTRANSFER => 'TRUE',
        CURLOPT_FOLLOWLOCATION => 'TRUE',
        CURLOPT_SSL_VERIFYPEER => 'FALSE',
        CURLOPT_POSTFIELDS => pathinfo($put_file,PATHINFO_BASENAME),
      ]);
    }
  }

  public function get_info($folder){
    $user = $this->user;
    $pass = $this->pass;
    $url = $this->url;
    $api = $this->api;
   
    $xmltag = <<< EOD
<?xml version="1.0" encoding="UTF-8"?>
 <d:propfind xmlns:d="DAV:" xmlns:oc="http://owncloud.org/ns" xmlns:nc="http://nextcloud.org/ns">
   <d:prop>
     <d:getlastmodified/>
     <d:getcontentlength/>
     <d:getcontenttype/>
     <oc:permissions/>
     <d:resourcetype/>
     <d:getetag/>
     <oc:fileid/>
   </d:prop>
 </d:propfind>
EOD;
   
    //対象フォルダIDを取得
    $ch = curl_init();
    curl_setopt_array($ch,[
      CURLOPT_CUSTOMREQUEST => 'PROPFIND',
      CURLOPT_URL => $url . $api . '/' . $folder,
      CURLOPT_USERPWD => $user . ':' . $pass,
      CURLOPT_RETURNTRANSFER => 'TRUE',
      CURLOPT_FOLLOWLOCATION => 'TRUE',
      CURLOPT_SSL_VERIFYPEER => 'FALSE',
      CURLOPT_POSTFIELDS => $xmltag,
    ]);

    //旧コード
    //curl_setopt($ch,CURLOPT_URL,$url.$api.$folder);
    //curl_setopt($ch,CURLOPT_CUSTOMREQUEST,'PROPFIND');
    //curl_setopt($ch,CURLOPT_POSTFIELDS,$xmltag);
    //curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    
    $xml = curl_exec($ch);
    curl_close($ch);

    var_dump($xml);

    //simplexml_load_string
    //$xml_obj = simplexml_load_file($xml,'SimpleXMLElement',LIBXML_NOCDATA);
    $xml_obj = new SimpleXMLElement($xml);
    //var_dump($xml_obj);
    $dom = new DOMDocument( '1.0' );
    $dom->loadXML( $xml_obj->asXML() );
    $dom->formatOutput = true;
    $nc = $xml_obj->getNamespaces(true);
    $xml_res = $xml_obj->children('d',true)->response->propstat->prop->children('oc',true)->fileid;
    $xml_obj=$dom->saveXML();
    //var_dump($xml_obj);
    //var_dump($nc);
    var_dump($xml_res);

    
    //$result = $xml->xpath('member/name');
    //$xml_obj = $xml_obj->xpath('');
    //var_dump($xml_obj);

    //TODO　要DEBUG
    //$json = json_encode($xmlObj);
    //$json = json_encode($xml);
    //$response = json_decode($json, true);
    //$response = json_encode($xml_obj, true);
    //$response = json_decode($xml_obj, true);
    
    
    //var_dump($response);
    
    //$folderID = $response["0"];
    //var_dump($folderID);

  }

  //タグ付け替え
  public function local_to_global($folder){
   $user = $this->user;
   $pass = $this->pass;
   $url = $this->url;
   $api = $this->api;
  
   $xmltag = <<< EOD
<?xml version="1.0" encoding="UTF-8"?>
 <d:propfind xmlns:d="DAV:" xmlns:oc="http://owncloud.org/ns" xmlns:nc="http://nextcloud.org/ns">
   <d:prop>
     <d:getlastmodified/>
     <d:getcontentlength/>
     <d:getcontenttype/>
     <oc:permissions/>
     <d:resourcetype/>
     <d:getetag/>
     <oc:fileid/>
   </d:prop>
 </d:propfind>
EOD;
  
   //対象フォルダIDを取得
   $ch = curl_init();
   curl_setopt_array($ch,[
     CURLOPT_CUSTOMREQUEST => 'PROPFIND',
     CURLOPT_URL => $url . $api . '/' . $folder,
     CURLOPT_USERPWD => $user . ':' . $pass,
     CURLOPT_RETURNTRANSFER => 'TRUE',
     CURLOPT_FOLLOWLOCATION => 'TRUE',
     CURLOPT_SSL_VERIFYPEER => 'FALSE',
     CURLOPT_POSTFIELDS => $xmltag,
   ]);
   $xml = curl_exec($ch);
   curl_close($ch);
   
   $xmlObj = simplexml_load_string($xml);
   $xmlObj = $xmlObj->children('d',true)->response->propstat->prop->children('oc',true)->fileid;
   
   //TODO　要DEBUG
   $json = json_encode($xmlObj);
   $response = json_decode($json, true);
   //var_dump($response);
   
   $folderID = $response["0"];
   
   //tagID:3=Local
   //tagID:4=Global

   //========== Local tag 削除 ==========
   $del_tagID='3';
   
   $ch = curl_init();
   curl_setopt_array($ch,[
     CURLOPT_CUSTOMREQUEST => 'DELETE',
     CURLOPT_URL => $url . 'remote.php/dav/systemtags-relations/files/'.$folderID.'/'.$del_tagID,
     CURLOPT_USERPWD => $user . ':' . $pass,
     CURLOPT_RETURNTRANSFER => 'TRUE',
     CURLOPT_FOLLOWLOCATION => 'TRUE',
     CURLOPT_SSL_VERIFYPEER => 'FALSE',
     CURLOPT_POSTFIELDS => $xmltag,
    ]);
   curl_exec($ch);
   curl_close($ch);
   
   //========== Global tag 追加 ==========
   $set_tagID='4';
   
   $ch = curl_init();
   curl_setopt_array($ch,[
     CURLOPT_CUSTOMREQUEST => 'PUT',
     CURLOPT_URL => $url . 'remote.php/dav/systemtags-relations/files/'.$folderID.'/'.$set_tagID,
     CURLOPT_USERPWD => $user . ':' . $pass,
     CURLOPT_RETURNTRANSFER => 'TRUE',
     CURLOPT_FOLLOWLOCATION => 'TRUE',
     CURLOPT_SSL_VERIFYPEER => 'FALSE',
     CURLOPT_POSTFIELDS => $xmltag,
    ]);
   curl_exec($ch);
   curl_close($ch);
  }

  public function del_tag($folder){
    $user = $this->user;
    $pass = $this->pass;
    $url = $this->url;
    $api = $this->api;

    $xmltag = <<< EOD
<?xml version='1.0' encoding='UTF-8'?>
 <d:propfind xmlns:d='DAV:' xmlns:oc='http://owncloud.org/ns' xmlns:nc='http://nextcloud.org/ns'>
   <d:prop>
     <d:getlastmodified/>
     <d:getcontentlength/>
     <d:getcontenttype/>
     <oc:permissions/>
     <d:resourcetype/>
     <d:getetag/>
     <oc:fileid/>
   </d:prop>
 </d:propfind>
EOD;

    $ch = curl_init();
    curl_setopt_array($ch,[
      CURLOPT_CUSTOMREQUEST => 'PROPFIND',
      CURLOPT_URL => $url . $api . '/' . $folder,
      CURLOPT_USERPWD => $user . ':' . $pass,
      CURLOPT_RETURNTRANSFER => 'TRUE',
      CURLOPT_FOLLOWLOCATION => 'TRUE',
      CURLOPT_SSL_VERIFYPEER => 'FALSE',
      CURLOPT_POSTFIELDS => $xmltag,
    ]);
    $xml = curl_exec($ch);
    curl_close($ch);
    var_dump($xml);
    
    $xmlObj = simplexml_load_string($xml);
    $xmlObj = $xmlObj->children('d',true)->response->propstat->prop->children('oc',true)->fileid;

    //TODO 要DEBUG
    $json = json_encode($xmlObj);
    $response = json_decode($json, true);
    #var_dump($response);
    
    $folderID = $response["0"];
    #$folderID='310';
    
    #tagID:3=Local
    #tagID:4=Global
    $DelTagID='4';
    
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $url.'remote.php/dav/systemtags-relations/files/'.$folderID.'/'.$DelTagID);
    curl_setopt($curl, CURLOPT_CUSTOMREQUEST, 'DELETE');
    curl_exec($curl);
    curl_close($curl);
    
    /* 
    フォルダの削除
    
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $url.'/remote.php/dav/files/admin/Share/Sharefolder/');
    curl_setopt($curl, CURLOPT_CUSTOMREQUEST, 'DELETE');
    curl_exec($curl);
    curl_close($curl);
    */
  }

  //フォルダの削除
  public function del_folder($folder){
    $user = $this->user;
    $pass = $this->pass;
    $url = $this->url;
    $api = $this->api;

    $ch = curl_init();
    curl_setopt_array($ch,[
      CURLOPT_CUSTOMREQUEST => 'DELETE',
      CURLOPT_URL => $url . $api . pathinfo($folder),
      CURLOPT_USERPWD => $user . ':' . $pass,
      CURLOPT_RETURNTRANSFER => 'TRUE',
      CURLOPT_FOLLOWLOCATION => 'TRUE',
      CURLOPT_SSL_VERIFYPEER => 'FALSE',
    ]);
    curl_exec($ch);
    curl_close($ch);
  }
}

$obj = new ExeApi();
$obj->run();

?>