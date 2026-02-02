# Tatoeba Dataset
**URL:** https://huggingface.co/datasets/Helsinki-NLP/tatoeba
**Page Title:** Helsinki-NLP/tatoeba · Datasets at Hugging Face
--------------------

The viewer is disabled because this dataset repo requires arbitrary Python code execution. Please consider
			removing the loading script and relying on automated data support (you can use convert_to_parquet from the datasets library). If this is not possible, please open a discussion for direct help.
[LINK: loading script](https://huggingface.co/docs/datasets/dataset_script)
[LINK: automated data support](https://huggingface.co/docs/datasets/repository_structure)
[LINK: convert_to_parquet](https://huggingface.co/docs/datasets/main/en/cli#convert-to-parquet)
[LINK: open a discussion](/datasets/Helsinki-NLP/tatoeba/discussions/new?title=Dataset+Viewer+issue%3A+DatasetWithScriptNotSupportedError&description=The+dataset+viewer+is+not+working.%0A%0AError+details%3A%0A%0A%60%60%60%0AError+code%3A+++DatasetWithScriptNotSupportedError%0A%0A%60%60%60%0A%0A%0A---%0A%0A%F0%9F%91%8B+Before+opening+the+discussion%2C+have+you+considered+removing+the+%5Bloading+script%5D%28https%3A%2F%2Fhuggingface.co%2Fdocs%2Fdatasets%2Fdataset_script%29+and+relying+on+%5Bautomated+data+support%5D%28https%3A%2F%2Fhuggingface.co%2Fdocs%2Fdatasets%2Frepository_structure%29%3F%0A%0AYou+can+use+%5Bconvert_to_parquet%5D%28https%3A%2F%2Fhuggingface.co%2Fdocs%2Fdatasets%2Fmain%2Fen%2Fcli%23convert-to-parquet%29+from+the+datasets+library.%0A%0A---%0A%0A%0Acc+%40albertvillanova+%40lhoestq+%40severo.)

## Dataset Card for Tatoeba

### Dataset Summary

Tatoeba is a collection of sentences and translations.
To load a language pair which isn't part of the config, all you need to do is specify the language code as pairs.
You can find the valid pairs in Homepage section of Dataset Description: http://opus.nlpl.eu/Tatoeba.php E.g.
dataset = load_dataset("tatoeba", lang1="en", lang2="he")
The default date is v2021-07-22, but you can also change the date with
dataset = load_dataset("tatoeba", lang1="en", lang2="he", date="v2020-11-09")

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

The languages in the dataset are:
- acm
- ady
- afb
- afh
- aii
- ain
- ajp
- akl
- aln
- ang
- aoz
- apc
- arq
- ary
- arz
- ast
- avk
- awa
- ayl
- bal
- bar
- ber
- bho
- bjn
- brx
- bua
- bvy
- bzt
- cay
- cbk
- ceb
- chg
- chn
- cho
- chr
- cjy
- ckb
- ckt
- cmn
- code
- cpi
- crh
- crk
- csb
- dng
- drt
- dsb
- dtp
- dws
- egl
- emx
- enm
- ext
- fkv
- frm
- fro
- frr
- fuc
- fur
- fuv
- gag
- gan
- gbm
- gcf
- gil
- gom
- gos
- got
- grc
- gsw
- hak
- haw
- hbo
- hif
- hil
- hnj
- hoc
- hrx
- hsb
- hsn
- iba
- ike
- ilo
- izh
- jam
- jbo
- jdt
- jpa
- kaa
- kab
- kam
- kek
- kha
- kjh
- kmr
- koi
- kpv
- krc
- krl
- ksh
- kum
- kxi
- kzj: Coastal Kadazan (deprecated tag; preferred value: Kadazan Dusun; Central Dusun ( dtp ))
- laa
- lad
- ldn
- lfn
- lij
- liv
- lkt
- lld
- lmo
- ltg
- lut
- lzh
- lzz
- mad
- mai
- max
- mdf
- mfe
- mgm
- mhr
- mic
- min
- mni
- mnw
- moh
- mvv
- mwl
- mww
- myv
- nah
- nan
- nch
- nds
- ngt
- ngu
- niu
- nlv
- nog
- non
- nov
- npi
- nst
- nus
- nys
- oar
- ofs
- ood
- orv
- osp
- ota
- otk
- pag
- pal
- pam
- pap
- pau
- pcd
- pdc
- pes
- phn
- pms
- pnb
- ppl
- prg
- quc
- qya
- rap
- rif
- rom
- rue
- sah
- scn
- sco
- sdh
- sgs
- shs
- shy
- sjn
- sma
- stq
- sux
- swg
- swh
- syc
- tet
- thv
- tig
- tlh
- tly
- tmr
- tmw
- toi
- tok
- tpi
- tpw
- tts
- tvl
- tyv
- tzl
- udm
- umb
- vec
- vep
- vro
- war
- wuu
- xal
- xqa
- yue
- zlm
- zsm
- zza

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

[More Information Needed]
[More Information Needed]
[More Information Needed]

### Annotations

[More Information Needed]
[More Information Needed]
[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to @abhishekkrthakur for adding this dataset.
[LINK: @abhishekkrthakur](https://github.com/abhishekkrthakur)

## Models trained or fine-tuned on Helsinki-NLP/tatoeba


--------------------