<font color="#87CEEB" size="5">? **����ʼ�**</font>  

### д��ǰ��

<details>
<summary><strong>? д��ǰ��</strong></summary>

---

~~Ϊ����Ӧѧϰָ�����ϴ�**git**�ֿ�~~������Ŀ�Ѿ��ϴ����ҵ�**github**�ֿ��գ�
```bash
https://github.com/wwwwwwwq/lianshidai-ml
```
Ȼ������csdnҲ����һƪ������git�����£���ӭ���ָ�����󣨣���  
```bash
https://blog.csdn.net/qq_30618989/article/details/145622471
```

---

**ע��**
- ��ǰĿ¼����6��.py�ļ���������һ����һ�£�
```bash
base.py��������
extend.py����չ�⣨Ĭ���õ�д��.json��ʽ����������ļ�ͷĬ�ϴ���ʱ�����
ResetDir.py������incoming_data���ļ���Ҳ�����ٻָ���û�з����״̬
TestFile.py�����Է��๦��
base_TestLog.py�������Դ��ı���.txt����ʽ�����־
extend_TestLog.py��������json��ʽ�����־
```
- ʹ�ýű���  
```python
#���ı��༭�����pycharm��vscode��vs2022�ȣ���
ֱ�����еĻ�·������Ĭ���ڵ�ǰ·����incoming_data

#����������
  #base����
    python base.py#ֱ�����У�·��Ĭ���ǵ�ǰ·����incoming_data
    
    #path���п��ޣ�����path����Ҫ�޸ĵ�·����Ҳ����˵������ݲ��ڵ�ǰ�ļ��еĻ�
    python base.py [path] test_file#�����ļ����๦��
    python base.py [path] test_log#������־�������

  #extend����
    python extend.py#ֱ�����У�·��Ĭ���ǵ�ǰ·����incoming_data

    #path���п��ޣ�����path����Ҫ�޸ĵ�·����Ҳ����˵������ݲ��ڵ�ǰ�ļ��еĻ�
    #text_flag���п��ޣ��������ɵĸ�ʽ��1�������ɴ��ı���.txt����2��������json��ʽ��Ĭ������json��ʽ
    python extend.py [path] test_file [text_flag]#�����ļ����๦��
    python extend.py [path] test_log [text_flag]#������־�������
```
- �����**��Ŀ���**��**ÿ������**�ȵȶ��ǻ���**��������**д�ģ�
~~��Ϊ������չ����ûʲô�ý���~~�������������ֻ����**��չ����**�Ĵ���
����û�о����˼·ʲô�ġ�
</details>

### ���

<details>
<summary><strong>? �������</strong></summary>

---

�����ҵ�һ����ml���⣨������֮ǰ��Ϊml���ⶼ��Ҫ��GPU��
Ȼ��Ҫ�ܼ���Сʱ�������ܵ���ģ�͵����֣�����������ȷʵ�ǣ���
Ȼ����ĿҲ�ܸ��ӣ�����֮ǰ�� ~~���ÿ�~~ �е�����ȴ����Ȼ������  
���Ҳ�����ָо������������Ļ���ϸһ����ʵ��python���ļ�������
�����⣬������Ҳ��΢�е�python���������Ի���дд�ա�  
</details>
<details>
<summary><strong>? ��Ŀ���</strong></summary>

---

��ž���˵����ô�����ļ���  
```
.quantum��������Ƭ��  
.holo��ȫϢͶӰ��  
.exo�������������ݣ�  
.chrono��ʱ�佺�ң�  
�Լ�δ֪��ʽ�Ŀ����ļ�  
```  
Ȼ��Ļ�����Ҫ��дһ��python��������ļ��ķ��࣬��δ֪�ļ�����
���룬��������ȫϢ��־��  
</details>

### �������

<details>
<summary><strong>? ����</strong></summary>

---

��ĿҪ����һ��incoming_data�ļ��У�����������Ŀû�������Ҿ�
��΢������һ����   
```bash
incoming_data/
    114514.holo
    #�е��������Ҫ����(
    alien_research.quantum
    #ʲô�������о�����
    imsb.xyz
    #�úú�
    mystery_signal.chrono
    #���۸������ź�
    unknown_species.exo
    #��������?
    uzio.opw
    #����Ϊ�Ҵ�
```
</details>
<details>
<summary><strong>? ���</strong></summary>

---
������ǰ�����Ŀ¼��ţ�  
```
.quantum �� ���� quantum_core/SECTOR-7G/
.holo �� ���� hologram_vault/CHAMBER-12F/
.exo �� ���� exobiology_lab/POD-09X/
.chrono �� ���� temporal_archive/VAULT-00T/
δ֪�ļ� �� ���� quantum_quarantine/ ����������ǰ׺�� ENCRYPTED_��
```
Ȼ�������ȫϢ��־��
```
��������������������������������������������������������������������  
�� ? Xia-III �ռ�վ���ݷֲ�ȫϢͼ ��
��������������������������������������������������������������������

����? incoming_data
��   ����? quantum_core
��   ��   ����? SECTOR-7G
��   ��   ��   ����? alien_research.quantum 
��   ����? quantum_quarantine
��   ��   ����?? ENCRYPTED_imsb.xyz

? SuperNova �� �����׼ʱ 2142-10-25T12:03:47
?? ���棺����ֱ�������ļ�����
```
</details>

### �������

?? �Ǿ������Ǿ�һ��һ���������ɣ�  
<details>
<summary><strong>? �����ļ�</strong></summary>

---

### ? �����߼�
- ### �����ļ�  
������**�����ļ�**�������ʵ�ܼ򵥣�ֱ��ͨ��os.listdir()�г�Ŀ¼�µ�
�����ļ���Ȼ��һ��һ���жϾͿ����ˡ�  
  - **����ӳ��**  
����֮ǰ��������Ԥ����һ�¡����ǿ����Ƚ���һ��**��׺�ֵ�**��������**��׺->
Ŀ¼**��ӳ�䡣����Ŀ¼�ǰ�����Ŀ¼�ģ����Һ��������־��ʱ��Ҫ������
ӡ��Ŀ¼�������ø�**tuple**����Ϊֵ�洢����Ŀ¼��  
    ```python
    #�洢��Ϊ��չ��������os.path.splitext���ص���'.ext'�����Լ���.��ͷ����ֵΪĿ¼���ֵ�
    #���ں�����־Ҫ��ȡÿ����Ŀ¼�����ƣ����������ֵ��tuple
    ext_dir={'.quantum':('quantum_core','SECTOR-7G'),'.holo':('hologram_vault','CHAMBER-12F'),'.exo':('exobiology_lab','POD-09X'),'.chrono':('temporal_archive','VAULT-00T')}
    
    #δ֪�ļ��洢Ŀ¼��Ҳ��tuple�洢
    unknownFile_dir=('quantum_quarantine',)#�Ӹ�,��ֹ��Ϊ������
    ```

  - **����ÿһ���ļ�**  
  ���������ǾͿ���**����ÿһ���ļ�**�ˡ���������process_file()����
  �������ļ������Ҵ���·����Ϊ������  
  ������������־��ʱ����������δ֪�ļ����������ܻ�ÿ�һ�㣬��������
  �ȴ����������б�һ��**����������֪��**��һ��**��������δ֪��**��  
    ```python
    #�����ļ�������·������������֪�����incoming_data�£�������Ĭ�ϱ���
    def process_files(directory='./incoming_data/'):
        #�½�һ�����б��洢�Ѿ�����õ��ļ�
        #����Ϊ�˿��ӻ���δ֪�ļ��ŵ����һ���������������б�
        knownFile_processed_files=[]
        unKnownFile_processed_files=[]
    ```
    ��������������os.listdir()�г���ǰĿ¼�µ������ļ��������ж��ˡ�
    �����Ȼ���һ���ļ�·��**filepath**��Ȼ������os.path.isfile(filepath)
    ��**�ж��Ƿ����ļ�**��������filename.startswith('.')�ж��Ƿ���.��ͷ
    ����ǵĻ�˵����**�����ļ�**����Ϊwindows��һ�㲻��.��ͷ��Ϊ�ļ�������
    ʱ��Ҫ�����  
    ```python
        #����Ŀ¼�µ������ļ�  
        for filename in os.listdir(directory):  
            #�����ļ�·��������os.path.isfile()���ж��Ƿ��ǺϷ��ļ�  
            filepath=os.path.join(directory, filename)  
      
            #���˵���ǺϷ��ļ������ļ���.��ͷ��������������ļ��������������ļ����ж���һ���ļ�  
            if not os.path.isfile(filepath) or filename.startswith('.'):  
                continue
    ```
    Ȼ������os.path.splitext(filename)[1].lower��ȡ
    ��׺�����ﲻֱ����filename.split('.')����Ϊ���ܻ�**����**������t.q.py)
    ������ȡ��.py�ĺ�׺�����ǻ��'q'��  
    ```python
            #����os.path.splitext��¼��չ����  
            #os.path.splitext���ص���һ���б�����չ���ڵڶ���Ԫ�أ���������filename[1]  
            #������Ŀû˵�Ƿ��Ǵ�д���������lower()ͳһСд����  
            ext=os.path.splitext(filename)[1].lower()
    ```
    ��ȡ��׺֮���ֱ���ж��Ƿ�����֪�ļ����ֵ����棬����ڵĻ��ͻ�ȡ·��
    **cat_dir**��**���ø���**��������**isUnknow=False**���:  
    ```python
            #�����չ��������չ���ֵ�����֪�ģ����ļ��洢��Ŀ¼���Ƕ�Ӧ��ֵ�Ե�ֵ���ļ����Ʋ��䣬isUnknown=False  
            if ext in ext_dir:  
                cat_dir=ext_dir[ext]  
                new_filename=filename  
                isUnknown=False#����isUnknown��Ϊ�˸�������־����õ�
    ```
    ����Ļ����洢·��**cat_dir**�ͱ��δ֪�ļ���·��������file������ǰ��
    ����**ENCRYPTED**�����**isUnknown=True**:  
    ```python
            #����Ļ����ļ��洢��Ŀ¼��unknownFile_dir��������Ҫ��ǰ׺��isUnknown=True  
            else:  
                cat_dir=unknownFile_dir  
                #���˵ԭ������ENCRYPTEDǰ׺����ô���־Ͳ��ñ䣨�������Ҳ²�ģ���Ŀû˵��Ҳ��֪��Ҫ��Ҫqwq��  
                if filename.split('_')[0]=='ENCRYPTED':  
                    new_filename=filename  
                else:  
                    new_filename=f'ENCRYPTED_{filename}'#��f-string���и�ʽ��  
                isUnknown=True  
    ```
    �������֪�ļ���δ֪�ļ�֮�����ǿ����Ȼ���һ���ļ�Ҫ�浽��Ŀ¼·��
    Ϊ**desDir_path**��Ȼ����os.makedirs(desDir_path)����Ŀ¼������
    ����Ѿ�����������Ҫ�ٴδ������������ǿ��ԼӸ�����**exist_ok=True**
    ���os.makedirs(desDir_path,exist_ok=True)�������Ļ������
    �������Ͳ��ᱨ������������һ����  
    ```python
            #����os.makedirs����Ŀ¼������Ѿ�����������Ҫ�ٴ���������Ӧ��exist_ok=True  
            os.makedirs(desDir_path, exist_ok=True) 
    ```
    Ȼ�������ٻ������յ��ļ�·��**desFile_path**����ΪҪ����shutil.move()�����ļ��ƶ�
    ����Ҫ����·�����в�����֮�������shutil.move()�����ƶ��ͺ���:  
    ```python
            #�������յ��ļ�·��  
            desFile_path=os.path.join(desDir_path,new_filename)  
      
            #����shutil.move�ƶ��ļ�  
            shutil.move(filepath, desFile_path)  
    ```
    ���ﲻ����Ƿ�����һ����ԭ���ǣ�����ƶ����ļ���desFile_path�Ѿ�
    ���ڣ���ô˵��֮ǰ��Ŀ¼����������ļ�Ҳ������һ���ģ����Բ����ܻ���
    ����������֡�  
      
    ֮��͸���֪�ļ���δ֪�ļ��б�append�ֵ�ͺ��ˣ�����洢cat_dir��
    **new_filename**��������֮��ͷ��������б�python��**����������
    �Ļ�ʵ�����Ƿ���һ����������������tuple**��  
    ```python
            #���б��¼��Ϣ�ֵ䣬�Ա�����log���  
            #����Ϊ�˿��ӻ���δ֪�ļ��ŵ����һ���������������б�  
            if not isUnknown:  
                knownFile_processed_files.append({'cat_dir':cat_dir,'new_filename':new_filename})  
            else:  
                unKnownFile_processed_files.append({'cat_dir': cat_dir, 'new_filename': new_filename})  
      
        #ѭ������֮�󷵻ش�������ļ���Ϣ�б�  
        return knownFile_processed_files,unKnownFile_processed_files
    ```
    �����Ǵ���ÿһ���ļ����������룺  
    ```python
        #����Ŀ¼�µ������ļ�  
        for filename in os.listdir(directory):  
            #�����ļ�·��������os.path.isfile()���ж��Ƿ��ǺϷ��ļ�  
            filepath=os.path.join(directory, filename)  
      
            #���˵���ǺϷ��ļ������ļ���.��ͷ��������������ļ��������������ļ����ж���һ���ļ�  
            if not os.path.isfile(filepath) or filename.startswith('.'):  
                continue  
      
            #����os.path.splitext��¼��չ����  
            #os.path.splitext���ص���һ���б�����չ���ڵڶ���Ԫ�أ���������filename[1]  
            #������Ŀû˵�Ƿ��Ǵ�д���������lower()ͳһСд����  
            ext=os.path.splitext(filename)[1].lower()  
      
            #�����չ��������չ���ֵ�����֪�ģ����ļ��洢��Ŀ¼���Ƕ�Ӧ��ֵ�Ե�ֵ���ļ����Ʋ��䣬isUnknown=False  
            if ext in ext_dir:  
                cat_dir=ext_dir[ext]  
                new_filename=filename  
                isUnknown=False#����isUnknown��Ϊ�˸�������־����õ�  
      
            #����Ļ����ļ��洢��Ŀ¼��unknownFile_dir��������Ҫ��ǰ׺��isUnknown=True  
            else:  
                cat_dir=unknownFile_dir  
                #���˵ԭ������ENCRYPTEDǰ׺����ô���־Ͳ��ñ䣨�������Ҳ²�ģ���Ŀû˵��Ҳ��֪��Ҫ��Ҫqwq��  
                if filename.split('_')[0]=='ENCRYPTED':  
                    new_filename=filename  
                else:  
                    new_filename=f'ENCRYPTED_{filename}'#��f-string���и�ʽ��  
                isUnknown=True  
      
            #�������յ�Ŀ¼·��  
            desDir_path=os.path.join(directory,*cat_dir)#���tuple  
      
            #����os.makedirs����Ŀ¼������Ѿ�����������Ҫ�ٴ���������Ӧ��exist_ok=True  
            os.makedirs(desDir_path, exist_ok=True)  
      
            #�������յ��ļ�·��  
            desFile_path=os.path.join(desDir_path,new_filename)  
      
            #����shutil.move�ƶ��ļ�  
            shutil.move(filepath, desFile_path)  
      
            #���б��¼��Ϣ�ֵ䣬�Ա�����log���  
            #����Ϊ�˿��ӻ���δ֪�ļ��ŵ����һ���������������б�  
            if not isUnknown:  
                knownFile_processed_files.append({'cat_dir':cat_dir,'new_filename':new_filename})  
            else:  
                unKnownFile_processed_files.append({'cat_dir': cat_dir, 'new_filename': new_filename})  
      
        #ѭ������֮�󷵻ش�������ļ���Ϣ�б�  
        return knownFile_processed_files,unKnownFile_processed_files  
    ```
������process_files�������������룺  
```python
#�����ļ�������·������������֪�����incoming_data�£�������Ĭ�ϱ���
def process_files(directory='./incoming_data/'):
    #�½�һ�����б��洢�Ѿ�����õ��ļ�
    #����Ϊ�˿��ӻ���δ֪�ļ��ŵ����һ���������������б�
    knownFile_processed_files=[]
    unKnownFile_processed_files=[]

    #����Ŀ¼�µ������ļ�
    for filename in os.listdir(directory):
        #�����ļ�·��������os.path.isfile()���ж��Ƿ��ǺϷ��ļ�
        filepath=os.path.join(directory, filename)

        #���˵���ǺϷ��ļ������ļ���.��ͷ��������������ļ��������������ļ����ж���һ���ļ�
        if not os.path.isfile(filepath) or filename.startswith('.'):
            continue

        #����os.path.splitext��¼��չ����
        #os.path.splitext���ص���һ���б�����չ���ڵڶ���Ԫ�أ���������filename[1]
        #������Ŀû˵�Ƿ��Ǵ�д���������lower()ͳһСд����
        ext=os.path.splitext(filename)[1].lower()

        #�����չ��������չ���ֵ�����֪�ģ����ļ��洢��Ŀ¼���Ƕ�Ӧ��ֵ�Ե�ֵ���ļ����Ʋ��䣬isUnknown=False
        if ext in ext_dir:
            cat_dir=ext_dir[ext]
            new_filename=filename
            isUnknown=False#����isUnknown��Ϊ�˸�������־����õ�

        #����Ļ����ļ��洢��Ŀ¼��unknownFile_dir��������Ҫ��ǰ׺��isUnknown=True
        else:
            cat_dir=unknownFile_dir
            #���˵ԭ������ENCRYPTEDǰ׺����ô���־Ͳ��ñ䣨�������Ҳ²�ģ���Ŀû˵��Ҳ��֪��Ҫ��Ҫqwq��
            if filename.split('_')[0]=='ENCRYPTED':
                new_filename=filename
            else:
                new_filename=f'ENCRYPTED_{filename}'#��f-string���и�ʽ��
            isUnknown=True

        #�������յ�Ŀ¼·��
        desDir_path=os.path.join(directory,*cat_dir)#���tuple

        #����os.makedirs����Ŀ¼������Ѿ�����������Ҫ�ٴ���������Ӧ��exist_ok=True
        os.makedirs(desDir_path, exist_ok=True)

        #�������յ��ļ�·��
        desFile_path=os.path.join(desDir_path,new_filename)

        #����shutil.move�ƶ��ļ�
        shutil.move(filepath, desFile_path)

        #���б��¼��Ϣ�ֵ䣬�Ա�����log���
        #����Ϊ�˿��ӻ���δ֪�ļ��ŵ����һ���������������б�
        if not isUnknown:
            knownFile_processed_files.append({'cat_dir':cat_dir,'new_filename':new_filename})
        else:
            unKnownFile_processed_files.append({'cat_dir': cat_dir, 'new_filename': new_filename})

    #ѭ������֮�󷵻ش�������ļ���Ϣ�б�
    return knownFile_processed_files,unKnownFile_processed_files
```  
</details>
<details>
<summary><strong>? ����ȫϢ��־</strong></summary>

---

### ? �����߼�
- ### ����ȫϢ��־  
  ������Ҫ����һ��**hologram.txt**��ȫϢ��־���ṹ����������ģ�  
  ```bash
  ��������������������������������������������������������������������  
  �� ? Xia-III �ռ�վ���ݷֲ�ȫϢͼ ��
  ��������������������������������������������������������������������
  
  ����? incoming_data
  ��   ����? quantum_core
  ��   ��   ����? SECTOR-7G
  ��   ��   ��   ����? alien_research.quantum 
  ��   ����? quantum_quarantine
  ��   ��   ����?? ENCRYPTED_imsb.xyz
  
  ? SuperNova �� �����׼ʱ 2142-10-25T12:03:47
  ?? ���棺����ֱ�������ļ�����
  ```
  ��ô�Ļ���Ҫ���������Ľṹ����ͷ�ͽ�β�������⣬�ؼ���Ҫ��δ����м�
  ����״Ŀ¼�ļ��ṹ��  
  - **Ԥ��������**  
    ��Ȼ��Ҫ���Ǵ���Ŀ¼���ļ��Ļ�����������Ҫ�õ���**�����ļ�**�л�ȡ��
    Ŀ¼���ļ����ơ�  
    <br>
    ��ô��Ȼ��Ҫ��¼��ӦĿ¼�µ��ļ����ƺ��Ƿ���δ֪�ļ������Ǿ�Ҫ���ֵ���
    ���档������python�Դ���dict����һ�����ǵ�ѡ����Ϊ��������**�Զ���ʼ��**
    �����ڴ�Ҳ����**��̬����**�ģ���һĿ¼һ��Ͳ���ʹ�ˣ���Ȼ����Ŀ¼�����޵ģ�
    ��������Ҫ����һ��һ�����������������ط��Ҿ�������һ��**collections**
    �������**defaultdict**�ֵ䣬������ʵ���������ᵽ�����⣺ 
    ```python
    from collections import defaultdict
    
    #��Ŀ¼�����ļ�
    #������defaultdict���洢�ļ���Ϣ��������ͨ���ֵ䣬��Ϊ��ͨ���ֵ��ʼ�����鷳���Ҳ��ܶ�̬����ռ�
    cat_groups=defaultdict(list)
    ```
    ���������Ǿͱ���**process_file()** �������ص� **processed_files**
    ���tuple(������Ϊ�˷������**files**����**processed_files**��)��Ȼ���
    **files[0]**��Ҳ������֪�ļ���ȡ��**dir**��**filename**������**symbol**���Ϊ'?'
    ��Ȼ���**symbol**��**filename**��append��cat_groups[dir]�ֵ��С��ٶ�δ֪�ļ�
    ����ͬ���Ĵ���**����δ֪�ļ��Ϳ��԰�δ֪�ļ��ŵ��ֵ����**����  
    ```python
      #����processed_files���ļ���Ϣ������Ŀ¼����Ϊ�����洢��־���ļ�����
      #�ȱ�����֪�ļ�
      for file_info in files[0]:
          dir=file_info['cat_dir']
          file=file_info['new_filename']
          symbol='?'
          cat_groups[dir].append({'symbol':symbol,'file':file})
  
      #�ٱ���δ֪�ļ�
      for file_info in files[1]:
          dir=file_info['cat_dir']
          file=file_info['new_filename']
          symbol='??'
          cat_groups[dir].append({'symbol':symbol,'file':file})
    ```
    ������Ԥ������������룺  
    ```python
      #��Ŀ¼�����ļ�
      #������defaultdict���洢�ļ���Ϣ��������ͨ���ֵ䣬��Ϊ��ͨ���ֵ��ʼ�����鷳���Ҳ��ܶ�̬����ռ�
      cat_groups=defaultdict(list)
  
      #����processed_files���ļ���Ϣ������Ŀ¼����Ϊ�����洢��־���ļ�����
      #�ȱ�����֪�ļ�
      for file_info in files[0]:
          dir=file_info['cat_dir']
          file=file_info['new_filename']
          symbol='?'
          cat_groups[dir].append({'symbol':symbol,'file':file})
  
      #�ٱ���δ֪�ļ�
      for file_info in files[1]:
          dir=file_info['cat_dir']
          file=file_info['new_filename']
          symbol='??'
          cat_groups[dir].append({'symbol':symbol,'file':file})
    ```
  - **�洢Ŀ¼���ļ���Ϣ**  
    ��������������Ҫ��һ���ˣ��Ǿ�������Ҫ���б����洢Ҫ��ӡ����Ϣ��
    ���ȳ�ʼ��**lines**��**��ʼ����Ϣ**��Ȼ���������Ŀ¼��Ϣ���ļ���Ϣ��
    ĩβ��Ϣ������Ժ��extend��lines�Ϳ����ˣ�  
    - **��ӡ��ʼ��Ϣ**
      ```python
       #��ӡ��ʼ��Ϣ�͸�Ŀ¼
         lines = [
             "������������������������������������������������������������������������������������������",
             "�� ? Xia-III �ռ�վ���ݷֲ�ȫϢͼ ��             ",
             "������������������������������������������������������������������������������������������",
             "",
             f"����? {os.path.basename(os.path.normpath(directory))}"#os.path.normpath�ǹ淶��Ŀ¼��os.path.basename��ȡĿ¼�����һ�����ּ�incoming_data
         ]   
      ```
    - **��ӡĿ¼���ļ���Ϣ**  
      ����������Ҫ**��ӡĿ¼���ļ���Ϣ**��������**��״�ṹ**����ʾ�ġ�
      ��ô����ô��ӡ�أ�����Ļ�����΢����һ��ai���ֽṹӦ����ô
      �洢��Ȼ��ai�Ļش��е㲻�����⡣��Ҫô����һֱ�ݹ鹹���������ݽṹ
      Ҫô����̫���ӣ��������ҵ�ʵ�����������Ĵ�������߼��������Ҹɴ�
      ���Լ��ִ�һ�����ˡ����ȳ�ʼ��һ��**dir_lines[]**�б����洢ÿһ��
      ����Ϣ��  
      ```python
          #��һ���б��¼ÿһ��
             dir_lines=[]
      ```
      ���ţ�����Ҫ��������Ԥ�����й����**cat_groups**�ֵ䣬�������е�**Ŀ¼��Ϣ**
      ��**�ļ���Ϣ**�ó����������ȱ���**cat_groups**�еļ���
      ����**dir**�洢��Ȼ�����ÿһ��dir�����Ƕ���ʼ��һ������**dir_start**��  
      ```python
      #�洢Ŀ¼���ļ���Ϣ���б�
         for dir in cat_groups:
             #��Ŀ¼����ʼ����
             dir_start = f'��   '
      ```
      �������ó�ÿһ��Ŀ¼�������º�ά���������д洢��  
      ```python
             #�洢Ŀ¼
             for child_dir in dir:
                 dir_lines.append(f'{dir_start}����? {child_dir}')
                 dir_start+=f'��   '
      ```
      Ȼ���ٴ����ļ���  
      ```python
             #��¼��־���ļ�����
             for filename in cat_groups[dir]:
                 #�洢�ļ�
                 dir_lines.append(f'{dir_start}����{filename['symbol']} {filename["file"]}')
      ```
      ����**dir_lines**��extend��**lines**�оͿ����ˣ�  
      ```python
         #����lines
         lines.extend(dir_lines)
      ```
      �����Ǵ�ӡĿ¼���ļ���Ϣ���������룺  
      ```python
        #��һ���б��¼ÿһ��
         dir_lines=[]

         #�洢Ŀ¼���ļ���Ϣ���б�
         for dir in cat_groups:
             #��Ŀ¼����ʼ����
             dir_start = f'��   '

             #�洢Ŀ¼
             for child_dir in dir:
                 dir_lines.append(f'{dir_start}����? {child_dir}')
                 dir_start+=f'��   '

             #��¼��־���ļ�����
             for filename in cat_groups[dir]:
                 #�洢�ļ�
                 dir_lines.append(f'{dir_start}����{filename['symbol']} {filename["file"]}')

         #����lines
         lines.extend(dir_lines)
      ```
      - **��ӡĩβ��Ϣ**
      ��ӡĩβ��Ϣ�ͺܼ��ˣ��ǵ�Ҫ����ʱ�����  
      ```python
         #���ʱ��;���
         timeAndClaim = [
             "",
             f"? SuperNova �� �����׼ʱ {time}",
             "?? ���棺����ֱ�������ļ�����"
         ]

         lines.extend(timeAndClaim)
      ```
    �����Ǵ洢Ŀ¼���ļ���Ϣ���������룺  
    ```python
    #��ӡ��ʼ��Ϣ�͸�Ŀ¼
    lines = [
        "������������������������������������������������������������������������������������������",
        "�� ? Xia-III �ռ�վ���ݷֲ�ȫϢͼ ��             ",
        "������������������������������������������������������������������������������������������",
        "",
        f"����? {os.path.basename(os.path.normpath(directory))}"#os.path.normpath�ǹ淶��Ŀ¼��os.path.basename��ȡĿ¼�����һ�����ּ�incoming_data
    ]

    #��һ���б��¼ÿһ��
    dir_lines=[]

    #�洢Ŀ¼���ļ���Ϣ���б�
    for dir in cat_groups:
        #��Ŀ¼����ʼ����
        dir_start = f'��   '

        #�洢Ŀ¼
        for child_dir in dir:
            dir_lines.append(f'{dir_start}����? {child_dir}')
            dir_start+=f'��   '

        #��¼��־���ļ�����
        for filename in cat_groups[dir]:
            #�洢�ļ�
            dir_lines.append(f'{dir_start}����{filename['symbol']} {filename["file"]}')

    #����lines
    lines.extend(dir_lines)

    #���ʱ��;���
    timeAndClaim = [
        "",
        f"? SuperNova �� �����׼ʱ {time}",
        "?? ���棺����ֱ�������ļ�����"
    ]

    lines.extend(timeAndClaim)
    ```
  - **����������־��Ϣ�ĺ���**  
  �������׼������֮�����ǾͿ��Թ���������־��Ϣ�ĺ����ˡ��ҽ�������
  Ϊgenerate_hologram_log()����������Ҫ����
  (files,time,dirctory='./incoming_data/')��Ϊ������Ȼ��������Ҫ����һ��
  **log_path**������Ϊд���ļ���·����  
  ```python
  #����ȫϢ��־�ļ�hologram_log.txt������·�����Ѵ�������ļ���Ϣ��log��ŵ�·������������֪�����incoming_data�£�������Ĭ�ϱ�����
  #����ѡ���ı���1�����ı���2����json��ʽ
  def generate_hologram_log(files,time,directory='./incoming_data/'):
      #log_path��¼�����־���ļ�·��
      log_path=os.path.join(directory,'hologram_log.txt')
  ```
  ����������**Ԥ����**��**�洢Ŀ¼���ļ���Ϣ**�������Ѿ�������ˡ�  
  <br>
  Ȼ�����һ������д�룬�����õ�����with open(......) as f:��д���ļ�
  ��Ϊ������ã���ȫ�������ģ��ķ�ʽ����д���ļ��ģ����ҿ��Դ���'w'������
  ��֤�޸����ļ���ͽ���رգ���ȫ�Ըߣ�  
  ```python
  #д����־
    #��utf-8���룬ȷ���ܴ������ĺ�Unicode����
    with open(log_path,'w',encoding='utf-8') as f:
        f.write('\n'.join(lines))#��\n�����б��ÿһ���ַ���
  ```
  �������й����������ˣ����Ը���generate_hologram_log�����������ˣ�  
  ```python
  #����ȫϢ��־�ļ�hologram_log.txt������·�����Ѵ�������ļ���Ϣ��log��ŵ�·������������֪�����incoming_data�£�������Ĭ�ϱ�����
  #����ѡ���ı���1�����ı���2����json��ʽ
  def generate_hologram_log(files,time,directory='./incoming_data/'):
      #log_path��¼�����־���ļ�·��
      log_path=os.path.join(directory,'hologram_log.txt')

    #��Ŀ¼�����ļ�
    #������defaultdict���洢�ļ���Ϣ��������ͨ���ֵ䣬��Ϊ��ͨ���ֵ��ʼ�����鷳���Ҳ��ܶ�̬����ռ�
    cat_groups=defaultdict(list)

    #����processed_files���ļ���Ϣ������Ŀ¼����Ϊ�����洢��־���ļ�����
    #�ȱ�����֪�ļ�
    for file_info in files[0]:
        dir=file_info['cat_dir']
        file=file_info['new_filename']
        symbol='?'
        cat_groups[dir].append({'symbol':symbol,'file':file})

    #�ٱ���δ֪�ļ�
    for file_info in files[1]:
        dir=file_info['cat_dir']
        file=file_info['new_filename']
        symbol='??'
        cat_groups[dir].append({'symbol':symbol,'file':file})

    #��ӡ��ʼ��Ϣ�͸�Ŀ¼
    lines = [
        "������������������������������������������������������������������������������������������",
        "�� ? Xia-III �ռ�վ���ݷֲ�ȫϢͼ ��             ",
        "������������������������������������������������������������������������������������������",
        "",
        f"����? {os.path.basename(os.path.normpath(directory))}"#os.path.normpath�ǹ淶��Ŀ¼��os.path.basename��ȡĿ¼�����һ�����ּ�incoming_data
    ]

    #��һ���б��¼ÿһ��
    dir_lines=[]

    #�洢Ŀ¼���ļ���Ϣ���б�
    for dir in cat_groups:
        #��Ŀ¼����ʼ����
        dir_start = f'��   '

        #�洢Ŀ¼
        for child_dir in dir:
            dir_lines.append(f'{dir_start}����? {child_dir}')
            dir_start+=f'��   '

        #��¼��־���ļ�����
        for filename in cat_groups[dir]:
            #�洢�ļ�
            dir_lines.append(f'{dir_start}����{filename['symbol']} {filename["file"]}')

    #����lines
    lines.extend(dir_lines)

    #���ʱ��;���
    timeAndClaim = [
        "",
        f"? SuperNova �� �����׼ʱ {time}",
        "?? ���棺����ֱ�������ļ�����"
    ]

    lines.extend(timeAndClaim)

    #д����־
    #��utf-8���룬ȷ���ܴ������ĺ�Unicode����
    with open(log_path,'w',encoding='utf-8') as f:
        f.write('\n'.join(lines))#��\n�����б��ÿһ���ַ���
  ```
</details>

### ��������

<details>
<summary><strong>? �������ֵ���������</strong></summary>

---

```python
import json
import shutil
import os
import sys
from collections import defaultdict
from datetime import datetime

# �洢��Ϊ��չ��������os.path.splitext���ص���'.ext'�����Լ���.��ͷ����ֵΪĿ¼���ֵ�
# ���ں�����־Ҫ��ȡÿ����Ŀ¼�����ƣ����������ֵ��tuple
ext_dir = {'.quantum': ('quantum_core', 'SECTOR-7G'), '.holo': ('hologram_vault', 'CHAMBER-12F'),
           '.exo': ('exobiology_lab', 'POD-09X'), '.chrono': ('temporal_archive', 'VAULT-00T')}

# δ֪�ļ��洢Ŀ¼��Ҳ��tuple�洢
unknownFile_dir = ('quantum_quarantine',)  # �Ӹ�,��ֹ��Ϊ������


# �����ļ�������·������������֪�����incoming_data�£�������Ĭ�ϱ���
def process_files(directory='./incoming_data/'):
  # �½�һ�����б��洢�Ѿ�����õ��ļ�
  # ����Ϊ�˿��ӻ���δ֪�ļ��ŵ����һ���������������б�
  knownFile_processed_files = []
  unKnownFile_processed_files = []

  # ����Ŀ¼�µ������ļ�
  for filename in os.listdir(directory):
    # �����ļ�·��������os.path.isfile()���ж��Ƿ��ǺϷ��ļ�
    filepath = os.path.join(directory, filename)

    # ���˵���ǺϷ��ļ������ļ���.��ͷ��������������ļ��������������ļ����ж���һ���ļ�
    if not os.path.isfile(filepath) or filename.startswith('.'):
      continue

    # ����os.path.splitext��¼��չ����
    # os.path.splitext���ص���һ���б�����չ���ڵڶ���Ԫ�أ���������filename[1]
    # ������Ŀû˵�Ƿ��Ǵ�д���������lower()ͳһСд����
    ext = os.path.splitext(filename)[1].lower()

    # �����չ��������չ���ֵ�����֪�ģ����ļ��洢��Ŀ¼���Ƕ�Ӧ��ֵ�Ե�ֵ���ļ����Ʋ��䣬isUnknown=False
    if ext in ext_dir:
      cat_dir = ext_dir[ext]
      new_filename = filename
      isUnknown = False  # ����isUnknown��Ϊ�˸�������־����õ�

    # ����Ļ����ļ��洢��Ŀ¼��unknownFile_dir��������Ҫ��ǰ׺��isUnknown=True
    else:
      cat_dir = unknownFile_dir
      # ���˵ԭ������ENCRYPTEDǰ׺����ô���־Ͳ��ñ䣨�������Ҳ²�ģ���Ŀû˵��Ҳ��֪��Ҫ��Ҫqwq��
      if filename.split('_')[0] == 'ENCRYPTED':
        new_filename = filename
      else:
        new_filename = f'ENCRYPTED_{filename}'  # ��f-string���и�ʽ��
      isUnknown = True

    # �������յ�Ŀ¼·��
    desDir_path = os.path.join(directory, *cat_dir)  # ���tuple

    # ����os.makedirs����Ŀ¼������Ѿ�����������Ҫ�ٴ���������Ӧ��exist_ok=True
    os.makedirs(desDir_path, exist_ok=True)

    # �������յ��ļ�·��
    desFile_path = os.path.join(desDir_path, new_filename)

    # ����shutil.move�ƶ��ļ�
    shutil.move(filepath, desFile_path)

    # ���б��¼��Ϣ�ֵ䣬�Ա�����log���
    # ����Ϊ�˿��ӻ���δ֪�ļ��ŵ����һ���������������б�
    if not isUnknown:
      knownFile_processed_files.append({'cat_dir': cat_dir, 'new_filename': new_filename})
    else:
      unKnownFile_processed_files.append({'cat_dir': cat_dir, 'new_filename': new_filename})

  # ѭ������֮�󷵻ش�������ļ���Ϣ�б�
  return knownFile_processed_files, unKnownFile_processed_files


# ����ȫϢ��־�ļ�hologram_log.txt������·�����Ѵ�������ļ���Ϣ��log��ŵ�·������������֪�����incoming_data�£�������Ĭ�ϱ�����
# ����ѡ���ı���1�����ı���2����json��ʽ
def generate_hologram_log(files, time, directory='./incoming_data/'):
  # log_path��¼�����־���ļ�·��
  log_path = os.path.join(directory, 'hologram_log.txt')

  # ��Ŀ¼�����ļ�
  # ������defaultdict���洢�ļ���Ϣ��������ͨ���ֵ䣬��Ϊ��ͨ���ֵ��ʼ�����鷳���Ҳ��ܶ�̬����ռ�
  cat_groups = defaultdict(list)

  # ����processed_files���ļ���Ϣ������Ŀ¼����Ϊ�����洢��־���ļ�����
  # �ȱ�����֪�ļ�
  for file_info in files[0]:
    dir = file_info['cat_dir']
    file = file_info['new_filename']
    symbol = '?'
    cat_groups[dir].append({'symbol': symbol, 'file': file})

  # �ٱ���δ֪�ļ�
  for file_info in files[1]:
    dir = file_info['cat_dir']
    file = file_info['new_filename']
    symbol = '??'
    cat_groups[dir].append({'symbol': symbol, 'file': file})

  # ��ӡ��ʼ��Ϣ�͸�Ŀ¼
  lines = [
    "������������������������������������������������������������������������������������������",
    "�� ? Xia-III �ռ�վ���ݷֲ�ȫϢͼ ��             ",
    "������������������������������������������������������������������������������������������",
    "",
    f"����? {os.path.basename(os.path.normpath(directory))}"
    # os.path.normpath�ǹ淶��Ŀ¼��os.path.basename��ȡĿ¼�����һ�����ּ�incoming_data
  ]

  # ��һ���б��¼ÿһ��
  dir_lines = []

  # �洢Ŀ¼���ļ���Ϣ���б�
  for dir in cat_groups:
    # ��Ŀ¼����ʼ����
    dir_start = f'��   '

    # �洢Ŀ¼
    for child_dir in dir:
      dir_lines.append(f'{dir_start}����? {child_dir}')
      dir_start += f'��   '

    # ��¼��־���ļ�����
    for filename in cat_groups[dir]:
      # �洢�ļ�
      dir_lines.append(f'{dir_start}����{filename['symbol']} {filename["file"]}')

  # ����lines
  lines.extend(dir_lines)

  # ���ʱ��;���
  timeAndClaim = [
    "",
    f"? SuperNova �� �����׼ʱ {time}",
    "?? ���棺����ֱ�������ļ�����"
  ]

  lines.extend(timeAndClaim)

  # д����־
  # ��utf-8���룬ȷ���ܴ������ĺ�Unicode����
  with open(log_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))  # ��\n�����б��ÿһ���ַ���


# ����ڽ����������У������и������Ѿ��������incoming_data
# ֱ�Ӹ���incoming_data_copy��incoming_data
def Reset():
  # ��try����жϵ�ǰ�Ƿ����incoming_data
  if os.path.exists('incoming_data/'):
    shutil.rmtree('incoming_data')
    shutil.copytree('incoming_data_copy', 'incoming_data')
    print('������')
  else:
    print('��û��incoming_data�ļ���')


# �ļ�������ԣ����ڽ�����ʹ��
def testFile(path='./incoming_data/'):
  # �����ļ�,���������б�洢�Ĵ����ļ�����Ϣ�������ļ���չ����Ӧ��Ŀ¼���ļ��������֣��ļ��Ƿ���δ֪�ļ����ļ������մ洢Ŀ¼��
  processed_files = process_files(path)
  print(processed_files)


# ��־������ԣ����ڽ�����ʹ��
def testLog():
  # ����ʱ�������ȷ�����룩
  # �������log
  timestampLog = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

  # �������һ���б�
  test_files = [{'cat_dir': ('test1', 'test2'), 'new_filename': 'test', 'isUnknown': False}]

  generate_hologram_log(test_files, timestampLog)


# �����򣬹��ڽ�����ʹ��
def main(path='./incoming_data/'):
  # ����ʱ�������ȷ�����룩
  # �������log
  timestampLog = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

  # �����ļ�,���������б�洢�Ĵ����ļ�����Ϣ�������ļ���չ����Ӧ��Ŀ¼���ļ��������֣��ļ��Ƿ���δ֪�ļ����ļ������մ洢Ŀ¼��
  processed_files = process_files(path)
  generate_hologram_log(processed_files, timestampLog)


# ����������л���ֱ����������ж�����Ϊ����ģ���ڽ�����ʹ��
if __name__ == '__main__':
  # Ĭ��·�����������������л����������������Ҹ�ʽ��python base.pyʱĬ��Ŀ¼��default_path
  default_path = 'incoming_data/'
  test_flag = False  # ��ʼ��״̬

  # ������������������������и����������е���
  # ��������������У����Ҹ�ʽ��python base.py directory���л�Ŀ¼
  # �����ʽ��python base.py test_file����test_log����Ŀ¼��Ĭ��Ŀ¼�����ҽ����ļ��������־����ĵ���
  # �����ʽ��python base.py directory test_file����test_log����ȸı�Ŀ¼�ֽ��е���
  if len(sys.argv) >= 2:
    # ���˵��һ��������test_file����test_log�Ļ���·��ΪĬ��·��
    if sys.argv[1] in ['test_file', 'test_log']:
      # ��test_flag������״̬
      test_flag = sys.argv[1]
    # ������Ŀ¼�Ļ���Ĭ��·����Ϊ����
    else:
      default_path = sys.argv[1]
      # ���˵��������test_file����test_log
      if len(sys.argv) >= 3:
        test_flag = sys.argv[2]
  # �������ֱ����pycharm����vscode���У�ֱ���������
  else:
    main(default_path)

  # ������ļ�����
  if test_flag == 'test_file':
    testFile()
  # �������־����
  elif test_flag == 'test_log':
    testLog()
```
</details>
<details>
<summary><strong>? ��չ���ֵ���������</strong></summary>

---

```python
import json
import shutil
import os
import sys
from collections import defaultdict
from datetime import datetime

#�洢��Ϊ��չ��������os.path.splitext���ص���'.ext'�����Լ���.��ͷ����ֵΪĿ¼���ֵ�
#���ں�����־Ҫ��ȡÿ����Ŀ¼�����ƣ����������ֵ��tuple
ext_dir={'.quantum':('quantum_core','SECTOR-7G'),'.holo':('hologram_vault','CHAMBER-12F'),'.exo':('exobiology_lab','POD-09X'),'.chrono':('temporal_archive','VAULT-00T')}

#δ֪�ļ��洢Ŀ¼��Ҳ��tuple�洢
unknownFile_dir=('quantum_quarantine',)#�Ӹ�,��ֹ��Ϊ������

#�����ļ�������·������������֪�����incoming_data�£�������Ĭ�ϱ���
def process_files(directory='./incoming_data/',time=None):
    #�½�һ�����б��洢�Ѿ�����õ��ļ�
    #����Ϊ�˿��ӻ���δ֪�ļ��ŵ����һ���������������б�
    knownFile_processed_files = []
    unKnownFile_processed_files = []

    #����Ŀ¼�µ������ļ�
    for filename in os.listdir(directory):
        #�����ļ�·��������os.path.isfile()���ж��Ƿ��ǺϷ��ļ�
        filepath=os.path.join(directory, filename)

        #���˵���ǺϷ��ļ������ļ���.��ͷ��������������ļ��������������ļ����ж���һ���ļ�
        if not os.path.isfile(filepath) or filename.startswith('.'):
            continue

        #����os.path.splitext��¼��չ����
        #os.path.splitext���ص���һ���б�����չ���ڵڶ���Ԫ�أ���������filename[1]
        #������Ŀû˵�Ƿ��Ǵ�д���������lower()ͳһСд����
        ext=os.path.splitext(filename)[1].lower()

        #�����չ��������չ���ֵ�����֪�ģ����ļ��洢��Ŀ¼���Ƕ�Ӧ��ֵ�Ե�ֵ���ļ����Ʋ��䣬isUnknown=False
        if ext in ext_dir:
            cat_dir=ext_dir[ext]
            new_filename=f'{time}_{filename}'
            isUnknown=False#����isUnknown��Ϊ�˸�������־����õ�
            #����ͬ��׺���뵽һ���ֵ��б�����
            pass
        #����Ļ����ļ��洢��Ŀ¼��unknownFile_dir��������Ҫ��ǰ׺��isUnknown=True
        else:
            cat_dir=unknownFile_dir
            #���˵ԭ������ENCRYPTEDǰ׺����ô���־Ͳ��ñ䣨�������Ҳ²�ģ���Ŀû˵��Ҳ��֪��Ҫ��Ҫqwq��
            if filename.split('_')[0]=='ENCRYPTED':
                new_filename=f'{time}_{filename}'
            else:
                new_filename=f'{time}_ENCRYPTED_{filename}'#��f-string���и�ʽ��
            isUnknown=True
            #����ͬ��׺���뵽һ���ֵ��б�����
            pass

        #�������յ�Ŀ¼·��
        desDir_path=os.path.join(directory,*cat_dir)#���tuple

        #����os.makedirs����Ŀ¼������Ѿ�����������Ҫ�ٴ���������Ӧ��exist_ok=True
        os.makedirs(desDir_path, exist_ok=True)

        #�������յ��ļ�·��
        desFile_path=os.path.join(desDir_path,new_filename)

        #����shutil.move�ƶ��ļ�
        shutil.move(filepath, desFile_path)

        #����Ϊ�˿��ӻ���δ֪�ļ��ŵ����һ���������������б�
        if not isUnknown:
            knownFile_processed_files.append({'cat_dir':cat_dir,'new_filename':new_filename})
        else:
            unKnownFile_processed_files.append({'cat_dir': cat_dir, 'new_filename': new_filename})

    #ѭ������֮�󷵻ش�������ļ���Ϣ�б�
    return knownFile_processed_files,unKnownFile_processed_files

#����ȫϢ��־�ļ�hologram_log.txt������·�����Ѵ�������ļ���Ϣ��log��ŵ�·������������֪�����incoming_data�£�������Ĭ�ϱ�����
#����ѡ���ı���1�����ı���2����json��ʽ
def generate_hologram_log(files,time,format_mode=1,directory='./incoming_data/'):
    #����Ǵ��ı�
    if format_mode==1:
        #log_path��¼�����־���ļ�·��
        log_path=os.path.join(directory,'hologram_log.txt')

        #��Ŀ¼�����ļ�
        #������defaultdict���洢�ļ���Ϣ��������ͨ���ֵ䣬��Ϊ��ͨ���ֵ��ʼ�����鷳���Ҳ��ܶ�̬����ռ�
        cat_groups=defaultdict(list)

        #����processed_files���ļ���Ϣ������Ŀ¼����Ϊ�����洢��־���ļ�����
        #�ȱ�����֪�ļ�
        for file_info in files[0]:
            dir=file_info['cat_dir']
            file=file_info['new_filename']
            symbol='?'
            cat_groups[dir].append({'symbol':symbol,'file':file})

        #�ٱ���δ֪�ļ�
        for file_info in files[1]:
            dir = file_info['cat_dir']
            file = file_info['new_filename']
            symbol = '??'
            cat_groups[dir].append({'symbol': symbol, 'file': file})

        #��ӡ��ʼ��Ϣ�͸�Ŀ¼
        lines = [
            "������������������������������������������������������������������������������������������",
            "�� ? Xia-III �ռ�վ���ݷֲ�ȫϢͼ ��             ",
            "������������������������������������������������������������������������������������������",
            "",
            f"����? {os.path.basename(os.path.normpath(directory))}"#os.path.normpath�ǹ淶��Ŀ¼��os.path.basename��ȡĿ¼�����һ�����ּ�incoming_data
        ]

        #��һ���б��¼ÿһ��
        dir_lines=[]

        #�洢Ŀ¼���ļ���Ϣ���б�
        for dir in cat_groups:
            #��Ŀ¼����ʼ����
            dir_start = f'��   '

            #�洢Ŀ¼
            for child_dir in dir:
                dir_lines.append(f'{dir_start}����? {child_dir}')
                dir_start+=f'��   '

            #��¼��־���ļ�����
            for filename in cat_groups[dir]:
                #�洢�ļ�
                dir_lines.append(f'{dir_start}����{filename['symbol']} {filename["file"]}')

        #����lines
        lines.extend(dir_lines)

        #���ʱ��;���
        timeAndClaim = [
            "",
            f"? SuperNova �� �����׼ʱ {time}",
            "?? ���棺����ֱ�������ļ�����"
        ]

        lines.extend(timeAndClaim)

        #д����־
        #��utf-8���룬ȷ���ܴ������ĺ�Unicode����
        with open(log_path,'w',encoding='utf-8') as f:
            f.write('\n'.join(lines))#��\n�����б��ÿһ���ַ���

    #���������JSON��ʽ
    elif format_mode==2:
        #log_path��¼�����־���ļ�·��
        log_path = os.path.join(directory, 'hologram_log.json')

        #��Ŀ¼�����ļ�
        #������defaultdict���洢�ļ���Ϣ��������ͨ���ֵ䣬��Ϊ��ͨ���ֵ��ʼ�����鷳���Ҳ��ܶ�̬����ռ�
        json_data = defaultdict(list)

        #����processed_files���ļ���Ϣ������Ŀ¼����Ϊ�����洢��־���ļ�����
        #�ȱ�����֪�ļ�
        for file_info in files[0]:
            dir_tuple=file_info['cat_dir']

            #��ȡ���ϲ��Ŀ¼
            #������Ŀû˵��Ŀ¼����������Ӧ����ȡ���ϲ�Ŀ¼
            top_dir=dir_tuple[0]

            #��ȡ�ļ���
            file=file_info['new_filename']

            #��ӵ�json_data��
            json_data[top_dir].append(file)

        #�ٱ���δ֪�ļ�
        for file_info in files[1]:
            dir_tuple=file_info['cat_dir']

            #��ȡ���ϲ��Ŀ¼
            #������Ŀû˵��Ŀ¼����������Ӧ����ȡ���ϲ�Ŀ¼
            top_dir=dir_tuple[0]

            #��ȡ�ļ���
            file=file_info['new_filename']

            #��ӵ�json_data��
            json_data[top_dir].append(file)

        #д��json�ļ���
        with open(log_path,'w',encoding='utf-8') as f:
            #indent����������������4��
            #ensure_ascii=False���������ascii����ַ�������
            #����json.dump���л��б�Ϊjson��ʽ����д���ļ�
            json.dump(dict(json_data),f,indent=4,ensure_ascii=False)

#����ڽ����������У������и������Ѿ��������incoming_data
#ֱ�Ӹ���incoming_data_copy��incoming_data
def Reset():
    #��try����жϵ�ǰ�Ƿ����incoming_data
    if os.path.exists('./incoming_data/'):
        shutil.rmtree('./incoming_data')
        shutil.copytree('incoming_data_copy','incoming_data')
        print('������')
    else:
        print('��û��incoming_data�ļ���')


#�ļ�������ԣ����ڽ�����ʹ��
def testFile(path='./incoming_data/'):
    # ����ʱ�������ȷ�����룩
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    # �����ļ�,���������б�洢�Ĵ����ļ�����Ϣ�������ļ���չ����Ӧ��Ŀ¼���ļ��������֣��ļ��Ƿ���δ֪�ļ����ļ������մ洢Ŀ¼��
    processed_files = process_files(path,timestamp)
    print(processed_files)

#��־������ԣ����ڽ�����ʹ��
def testLog(format_mode=1):
    # ����ʱ�������ȷ�����룩
    # �������log
    timestampLog = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    # �������һ���б�
    test_files = ([{'cat_dir': ('knowntest1', 'knowntest2'), 'new_filename': 'knowntest'}],[{'cat_dir': ('unKnowntest1', 'unKnowntest2'), 'new_filename': 'unknowntest'}])

    generate_hologram_log(test_files,timestampLog,format_mode)

#�����򣬹��ڽ�����ʹ��
def main(path='./incoming_data/',format_mode=2):
    # ����ʱ�������ȷ�����룩
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    # �������log
    timestampLog = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    # �����ļ�,���������б�洢�Ĵ����ļ�����Ϣ�������ļ���չ����Ӧ��Ŀ¼���ļ��������֣��ļ��Ƿ���δ֪�ļ����ļ������մ洢Ŀ¼��
    processed_files = process_files(path,timestamp)
    generate_hologram_log(processed_files,timestampLog,format_mode)

#����������л���ֱ����������ж�����Ϊ����ģ���ڽ�����ʹ��
if __name__=='__main__':
    #Ĭ��·�����������������л����������������Ҹ�ʽ��python base.pyʱĬ��Ŀ¼��default_path
    default_path='./incoming_data/'
    test_flag=False#��ʼ��״̬
    text_flag=1#��ʼ���ĵ�״̬

    #������������������������и����������е���
    #��������������У����Ҹ�ʽ��python base.py directory���л�Ŀ¼
    #�����ʽ��python base.py test_file����test_log����Ŀ¼��Ĭ��Ŀ¼�����ҽ����ļ��������־����ĵ���
    #�����ʽ��python base.py directory test_file����test_log����ȸı�Ŀ¼�ֽ��е���
    if len(sys.argv)>=2:
        #���˵��һ��������test_file����test_log�Ļ���·��ΪĬ��·��
        if sys.argv[1] in ['test_file','test_log']:
            #��test_flag������״̬
            test_flag=sys.argv[1]
            if len(sys.argv)>=3 and sys.argv[1]=='test_log':
                if sys.argv[2] in ['1','2']:
                    text_flag=int(sys.argv[2])
        #���˵��һ�����������ֵĻ�
        elif sys.argv[1] in ['1','2']:
            text_flag=int(sys.argv[1])
        #������Ŀ¼�Ļ���Ĭ��·����Ϊ����
        else:
            default_path=sys.argv[1]
            #���˵��������test_file����test_log
            if len(sys.argv)>=3:
                if sys.argv[2] in ['test_file','test_log']:
                    test_flag=sys.argv[2]
                    if len(sys.argv)>=4:
                        if sys.argv[3] in ['1','2']:
                            text_flag=int(sys.argv[3])
                elif sys.argv[2] in ['1','2']:
                    text_flag=int(sys.argv[2])

        # ������ļ�����
        if test_flag == 'test_file':
            testFile()
        # �������־����
        elif test_flag == 'test_log':
            testLog(text_flag)
        else:
            main(default_path,text_flag)
    #�������ֱ����pycharm����vscode���У�ֱ���������
    else:
        main(default_path)
```
</details>

### ���н�ͼ

<details>
<summary><strong>? �ļ�����������н�ͼ</strong></summary>

---

### ��������  
  
- **ԭ��**��
  
![img_2.png](image/img_2.png)  
  
- **֮��**:  
  
**������**��
  
![img.png](image/img.png)  
  
**���к�**��  
  
![img_1.png](image/img_1.png)   
  
---
  
### ��չ����  
  
- **ԭ��**��  
  
![img_2.png](image/img_2.png)  
  
- **֮��**��  
  
**������**��  
  
![img_4.png](image/img_4.png)  
  
**���к�**��  
  
![img_3.png](image/img_3.png)  
</details>

<details>
<summary><strong>? ��־����������н�ͼ</strong></summary>

---

### ��������  
  
**�����У�**  
  
![img_5.png](image/img_5.png)  
  
**���к�**  
  
![img_6.png](image/img_6.png)   
  
---  
  
### ��չ����  
  
- **���ı���.txt����ʽ**��  
    
  **�����У�**  
    
  ![img_7.png](image/img_7.png)  
    
  **���к�**   
    
  ![img_8.png](image/img_8.png)    
    
- **json��ʽ**��  
     
  **�����У�**   
    
  ![img_9.png](image/img_9.png)   
    
  **���к�**    
    
  ![img_10.png](image/img_10.png)  
    
</details>
<details>
<summary><strong>? �������н�ͼ</strong></summary>

---

### ��������
  
- **����ǰ**   
  
![img_2.png](image/img_2.png)  
- **���к�**  
    
  **������**��  
    
  ![img_11.png](image/img_11.png)    
    
  **���к�**��    
    
  ![img_12.png](image/img_12.png)    
    
  **��־**��    
  ![img_13.png](image/img_13.png)    
    
---

### ��չ����  
  
- **���ı���.txt����ʽ**    
      
  - **������**    
      
    ![img_15.png](image/img_15.png)  
      
  - **���к�**    
      
    ![img_16.png](image/img_16.png)    
      
  - **��־**    
       
    ![img_17.png](image/img_17.png)    
      
- **json��ʽ**    
      
  - **������**    
      
    ![img_18.png](image/img_18.png)  
    
  - **���к�**    
      
    ![img_19.png](image/img_19.png)    
      
  - **��־**    
       
    ![img_20.png](image/img_20.png)    
      
</details>

### �ܽ�
  
<details>
<summary><strong>? �ܽ�</strong></summary>
���⻹�Ǻܿ���python���ļ����������ģ��ܺõ���?��  
���񵼳���pdf��ʱ���е�bug�������ܽᱻ���ˣ���  
</details>