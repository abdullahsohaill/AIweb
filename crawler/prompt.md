PROMPT to LLM: Now the thing is that ive made much progress in terms of the project. for cloud AI services, now im collecting the function calls endpoints etc and same for local AI

cloud AI:"

Service Name	URL	Base Domain	Auth Method	Key Endpoints	Payload Parameters	SDK Function Calls	Use Cases	Network Fingerprints
Google Vertex AI	https://cloud.google.com/vertex-ai	aiplatform.googleapis.com	OAuth2 Bearer (Google IAM)	POST .../models/{model}:generateContent, POST .../endpoints/{id}:predict	contents, role, parts, instances, parameters	model.generate_content(), endpoint.predict()	Enterprise GenAI, Custom ML Training	aiplatform.googleapis.com, :predict, :generateContent
Google AI Studio (Gemini)	https://aistudio.google.com	generativelanguage.googleapis.com	API Key (Header: x-goog-api-key)	POST /v1beta/models/{model}:generateContent, POST /v1beta/interactions	contents, parts, tools, generationConfig, safetySettings	client.models.generate_content()	Prototyping, Chatbots, Multimodal Agents	generativelanguage.googleapis.com, :generateContent, x-goog-api-key
Google Cloud Vision	https://cloud.google.com/vision	vision.googleapis.com	OAuth2 / API Key	POST /v1/images:annotate	requests, image, content, features, type	ImageAnnotatorClient.batch_annotate_images()	OCR, Label Detection, Face Detection	vision.googleapis.com, /images:annotate
Google Speech-to-Text	https://cloud.google.com/speech-to-text	speech.googleapis.com	OAuth2 / API Key	POST /v1/speech:recognize, POST /v1/speech:longrunningrecognize	config, audio, encoding, sampleRateHertz	SpeechClient.recognize()	Audio Transcription, Captioning	speech.googleapis.com, :recognize
Google Text-to-Speech	https://cloud.google.com/text-to-speech	texttospeech.googleapis.com	OAuth2 / API Key	POST /v1/text:synthesize	input, text, voice, audioConfig	TextToSpeechClient.synthesize_speech()	Voice Generation, Accessibility	texttospeech.googleapis.com, :synthesize
Google Translation API	https://cloud.google.com/translate	translation.googleapis.com	OAuth2 / API Key	POST /v3/projects/{id}:translateText	contents, sourceLanguageCode, targetLanguageCode	TranslationServiceClient.translate_text()	Language Translation	translation.googleapis.com, :translateText
Google Natural Language	https://cloud.google.com/natural-language	language.googleapis.com	OAuth2 / API Key	POST /v1/documents:analyzeEntities, POST /v1/documents:analyzeSentiment	document, content, type, encodingType	LanguageServiceClient.analyze_sentiment()	Sentiment Analysis, Entity Extraction	language.googleapis.com, :analyze
Google Document AI	https://cloud.google.com/document-ai	documentai.googleapis.com	OAuth2	POST /v1/projects/{id}/locations/{loc}/processors/{id}:process	rawDocument, content, mimeType	DocumentProcessorServiceClient.process_document()	Invoice Parsing, Form OCR	documentai.googleapis.com, :process
Dialogflow CX	https://cloud.google.com/products/conversational-agents	dialogflow.googleapis.com	OAuth2	POST /v3/projects/{id}/locations/{loc}/agents/{id}/sessions/{id}:detectIntent	queryInput, text, session, queryParams	SessionsClient.detect_intent()	Conversational AI, Chatbots	dialogflow.googleapis.com, :detectIntent
Google Video Intelligence	https://cloud.google.com/video-intelligence	videointelligence.googleapis.com	OAuth2	POST /v1/videos:annotate	inputUri, features, videoContext	VideoIntelligenceServiceClient.annotate_video()	Video Labeling, Shot Detection	videointelligence.googleapis.com, :annotate
Google AI Genkit	https://firebase.google.com/docs/genkit	(Self-hosted / Cloud Run)	Google IAM (OIDC)	POST /flow/{flowName}	data	genkit.runFlow()	AI Flow Orchestration, TypeScript Agents	/flow/, genkit
Microsoft Translator	https://www.microsoft.com/en-us/translator	api.cognitive.microsofttranslator.com	API Key (Ocp-Apim-Subscription-Key)	POST /translate?api-version=3.0	text, to, from	requests.post(url, json=[{'text':...}])	Real-time Translation	api.cognitive.microsofttranslator.com, /translate
Azure AI Services	https://azure.microsoft.com/products/ai-services	{custom}.cognitiveservices.azure.com	API Key (Ocp-Apim-Subscription-Key)	POST /vision/v3.2/analyze, POST /text/analytics/v3.1/sentiment	visualFeatures, documents, analysisInput	client.analyze_image(), client.analyze_sentiment()	Vision, Language, Content Safety	cognitiveservices.azure.com, /analyze
MS Copilot Studio	https://copilotstudio.microsoft.com	directline.botframework.com	Bearer Token (Direct Line Secret)	POST /v3/directline/conversations/{conversationId}/activities	type, text, from, value	Connection.postActivity()	Custom Chatbots, Copilots	directline.botframework.com, /conversations
Azure AI Video Indexer	https://vi.microsoft.com	api.videoindexer.ai	Access Token (Authorization: Bearer)	POST /{loc}/Accounts/{id}/Videos, GET /{loc}/Accounts/{id}/Videos/{videoId}/Index	privacy, videoUrl, language	client.upload_video(), client.get_video_index()	Video Insights, Transcription	api.videoindexer.ai, /Videos/
Cloudflare AI	https://ai.cloudflare.com	api.cloudflare.com	API Token (Authorization: Bearer)	POST /client/v4/accounts/{id}/ai/run/@cf/{model}	prompt, messages, stream	ai.run()	Edge Inference (Llama, Stable Diff)	api.cloudflare.com, /ai/run/
OpenAI API	https://openai.com/api	api.openai.com	API Key (Header: Authorization: Bearer sk-...)	POST /v1/chat/completions, POST /v1/images/generations, POST /v1/audio/transcriptions	model, messages, role, content, tools, response_format	client.chat.completions.create(), client.images.generate()	LLM Chat, DALL-E 3 Image Gen, Whisper Audio, Agents	api.openai.com, /v1/chat/completions, /v1/images/generations, Authorization: Bearer
Perplexity API	https://www.perplexity.ai/settings/api	api.perplexity.ai	API Key (Header: Authorization: Bearer pplx-...)	POST /chat/completions, POST /search	model (sonar-pro), messages, return_citations, search_domain_filter	client.chat.completions.create()	Online Search-Grounded LLM, Real-time Citations	api.perplexity.ai, /chat/completions, pplx-
Remove.bg API	https://www.remove.bg	api.remove.bg	API Key (Header: X-Api-Key)	POST /v1.0/removebg	image_file, image_url, size, type, format	removebg.remove_background_from_file()	Background Removal, Image Masking	api.remove.bg, /v1.0/removebg, X-Api-Key
Baidu Qianfan (Ernie)	https://cloud.baidu.com/doc/WENXINWORKSHOP	aip.baidubce.com	Access Token (Query param: ?access_token=...)	POST /rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions, POST /rpc/2.0/ai_custom/v1/wenxinworkshop/embeddings	messages, stream, temperature, user_id	erniebot.ChatCompletion.create()	Chinese LLM (Ernie 4.0), Enterprise Chat	aip.baidubce.com, /rpc/2.0/ai_custom, /wenxinworkshop/
NVIDIA NIM	https://build.nvidia.com	integrate.api.nvidia.com	API Key (Header: Authorization: Bearer nvapi-...)	POST /v1/chat/completions, POST /v1/embeddings	model, messages, max_tokens, temperature	client.chat.completions.create() (OpenAI-compatible)	High-performance Inference (Llama 3, Mistral, BioNeMo)	integrate.api.nvidia.com, /v1/chat/completions, nvapi-
IBM Watsonx	https://www.ibm.com/watsonx	us-south.ml.cloud.ibm.com	IAM Token (Header: Authorization: Bearer)	POST /ml/v1/text/generation?version=2023-05-29	model_id, input, parameters, project_id	model.generate_text()	Enterprise GenAI, Governance, RAG	ml.cloud.ibm.com, /ml/v1/text/generation, watsonx
Brave Search AI	https://search.brave.com	api.search.brave.com	API Key (Header: X-Subscription-Token)	GET /res/v1/web/search, GET /res/v1/summarizer/search	q, summary=true, count	requests.get()	Search Summarization, RAG Data Source	api.search.brave.com, /res/v1/web, X-Subscription-Token
DeepL API	https://www.deepl.com	api-free.deepl.com	API Key (Header: Authorization: DeepL-Auth-Key)	POST /v2/translate, POST /v2/document	text, target_lang, source_lang, glossary_id	translator.translate_text()	High-Accuracy Translation, Document Localization	api-free.deepl.com, api.deepl.com, /v2/translate
Grammarly (Internal)	https://www.grammarly.com	data.grammarly.com	Cookie / WebSocket	WSS /remotev1, POST /v1/batch	submit_ot, docid, rev, text_deltas	N/A (Internal WebSocket)	Grammar Checking, Tone Rewrite, G-Keyboard	data.grammarly.com, /remotev1, grammar-check
Tawk.to AI	https://www.tawk.to	wss.tawk.to	Cookie / Bearer (Web Internal)	POST /v1/chat-ai/suggest-reply, POST /v1/chat-ai/summarize	conversation_history, prompt	N/A (Internal WebSocket/REST)	AI Chat Agent Assistance, Summarization	wss.tawk.to, /chat-ai/, suggest-reply
Hugging Face Inference API	https://huggingface.co/inference-api	api-inference.huggingface.co	API Key (Header: Authorization: Bearer hf_...)	POST /v1/chat/completions, POST /pipeline/{task}/{model}	model, messages, inputs, parameters	client.chat.completions.create(), hf_api.inference_api.run_inference()	Model Hosting, Inference, Open Source Models	api-inference.huggingface.co, /v1/chat/completions, /pipeline/
DeepSeek API	https://api-docs.deepseek.com	api.deepseek.com	API Key (Header: Authorization: Bearer)	POST /chat/completions, POST /beta/completions	model, messages, stream, thinking	client.chat.completions.create()	Reasoning (R1), Code Generation, OpenAI-Compatible Chat	api.deepseek.com, /chat/completions
Gamma App	https://gamma.app	gamma.app	Bearer Token (Web Internal)	POST /api/decks/create, POST /api/cards/generate	topic, theme_id, deck_type, card_data	N/A (Web/Internal)	AI Presentation & Website Generation	gamma.app/api, /decks/create
ElevenLabs	https://beta.elevenlabs.io	api.elevenlabs.io	API Key (Header: xi-api-key)	POST /v1/text-to-speech/{voice_id}, POST /v1/audio-isolation	text, model_id, voice_settings, audio_file	client.text_to_speech.convert()	Voice Synthesis, Voice Cloning, Audio Isolation	api.elevenlabs.io, /text-to-speech, xi-api-key
Fotor AI	https://www.fotor.com	open-api.fotor.com	API Key (Header: Authorization: Bearer)	POST /v1/remove_bg, POST /v1/enhance	image_url, type, sync	requests.post(url, json=data)	Image Enhancement, Background Removal, Generation	open-api.fotor.com, /v1/remove_bg
ZeroGPT	https://zerogpt.com	zerogpt.com	Bearer Token (Web Internal)	POST /api/detect/text	text, input_type	N/A (Web/Internal)	AI Content Detection, Plagiarism Checking	zerogpt.com/api/detect
Blackbox AI	https://blackbox.ai	www.blackbox.ai	Cookie / Bearer (Web Internal)	POST /api/chat	messages, code_context, playground_mode	N/A (Web/Internal)	Code Search, Autocomplete, Agent Chat	www.blackbox.ai/api/chat
Face Swap AI	https://aifaceswap.io	api.aifaceswap.io	Bearer/Cookie (Web Internal)	POST /api/swap	source_image, target_image	N/A (Web/Internal)	Face Swapping, Image Manipulation	api.aifaceswap.io, /swap
Cutout.pro	https://www.cutout.pro	www.cutout.pro	API Key (Header: APIKEY)	POST /api/v1/matting, POST /api/v1/cartoonSelfie	file, type, mattingType	requests.post(url, files=files)	Image Segmentation, Video Background Removal	www.cutout.pro/api/v1
Alibaba DashScope (Qwen)	https://dashscope.console.aliyun.com	dashscope.aliyuncs.com	API Key (Header: Authorization: Bearer)	POST /api/v1/services/aigc/text-generation/generation, POST /api/v1/services/aigc/multimodal-generation/generation	model (qwen-max), input, parameters, messages	dashscope.Generation.call(), dashscope.MultiModalConversation.call()	Chinese/English LLM, Vision-Language Tasks	dashscope.aliyuncs.com, /text-generation/generation
Tencent Hunyuan	https://cloud.tencent.com/document/product/1729	hunyuan.tencentcloudapi.com	Tencent Cloud Auth (SigV3 in Header/Query)	POST / (Action=ChatCompletions)	Messages, Model, Stream, Temperature, TopP	client.ChatCompletions()	Enterprise Chat, WeChat Integration, Content Gen	hunyuan.tencentcloudapi.com, Action=ChatCompletions
Box AI	https://box.com/ai	api.box.com	OAuth2 (Header: Authorization: Bearer)	POST /2.0/ai/ask, POST /2.0/ai/text_gen, POST /2.0/ai/extract	prompt, items (file scopes), mode, dialogue_history	client.ai.ask(), client.ai.text_gen()	Document Summarization, Q&A on Enterprise Data	api.box.com, /2.0/ai/ask, /2.0/ai/text_gen
Salesforce Einstein	https://www.salesforce.com	api.einstein.ai	OAuth2 / JWT	POST /v2/language/intent, POST /v2/vision/predict	modelId, document, sampleId	client.predict()	CRM Automation, Lead Scoring, Sentiment Analysis	api.einstein.ai, /v2/language, /v2/vision
Zendesk AI	https://zendesk.com	{subdomain}.zendesk.com	API Key / OAuth	POST /api/v2/answer_bot/resolutions, POST /api/v2/chat/completions	query, ticket_context, input	client.answer_bot.create_resolution()	Customer Support Automation, Ticket Triage	zendesk.com, /api/v2/answer_bot
OVHcloud AI Endpoints	https://endpoints.ai.cloud.ovh.net	{model}.endpoints.kepler.ai.cloud.ovh.net	API Token (Header: Authorization: Bearer)	POST /api/openai_compat/v1/chat/completions	messages, model, stream	client.chat.completions.create() (OpenAI-compatible)	Hosted Open Source Models (Mistral, Llama)	endpoints.kepler.ai.cloud.ovh.net, /openai_compat/v1
JD.com NeuHub (OxyGent)	https://oxygent.jd.com	aiapi.jd.com	API Key (Query: ?access_token=...)	POST /jdai/sentiment, POST /jdai/tts	text, type, audio_config	N/A (REST)	Retail AI, Sentiment Analysis, Supply Chain AI	aiapi.jd.com, /jdai/
Braze AI (Sage)	https://www.braze.com	sdk.iad-01.braze.com	API Key (Query param/Body)	POST /api/v3/data/track, POST /api/v3/content_cards/sync	events, attributes, purchases	braze.initialize(), braze.logCustomEvent()	Marketing Automation, Predictive Churn	sdk.iad-01.braze.com, /data/track
Miro AI	https://miro.com	api.miro.com	OAuth2 (Header: Authorization: Bearer)	POST /v2/boards/{id}/items (with AI types)	content, type, geometry	client.create_shape_with_text() (indirect AI use)	Mind Mapping, Clustering, Diagramming	api.miro.com/v2
Webex AI Agents	https://webex.com	webexapis.com	Bearer Token (OAuth2)	GET /v1/meeting-transcripts/{id}, GET /v1/meetings/{id}/summary	meetingId, summary_format	sdk.meetings.get_summary()	Meeting Summarization, Action Items	webexapis.com, /v1/meeting-transcripts
Cloudinary AI	https://cloudinary.com	api.cloudinary.com	API Key / Sig (Basic Auth)	POST /v1_1/{cloud_name}/image/upload, POST /v1_1/{cloud_name}/video/upload	file, background_removal, categorization, ocr	cloudinary.uploader.upload()	AI Image Transformations, BG Removal, Tagging	api.cloudinary.com, /image/upload, /video/upload
DeepAI	https://deepai.org	api.deepai.org	API Key (Header: api-key)	POST /api/text2img, POST /api/summarization	text, image, grid_size	requests.post()	Text-to-Image, Text Generation, Summarization	api.deepai.org, /api/text2img
PhotoRoom API	https://photoroom.com	image-api.photoroom.com	API Key (Header: x-api-key)	POST /v1/remove-background, POST /v1/instant-backgrounds	image_file, background_prompt, format, size	photoroom.remove_background()	High-Fidelity Background Removal, Product AI	image-api.photoroom.com, /v1/remove-background
GPTZero API	https://gptzero.me	api.gptzero.me	API Key (Header: x-api-key)	POST /v2/predict/text, POST /v2/predict/file	document, version	client.predict()	AI Content Detection, Plagiarism Checking	api.gptzero.me, /v2/predict
Doubao (Volcengine)	https://team.doubao.com/en/special/doubao_1_5_pro	ark.cn-beijing.volces.com	API Key (Header: Authorization: Bearer)	POST /api/v3/chat/completions	model (ep-...), messages, stream	client.chat.completions.create() (OpenAI-compatible)	Chinese LLM, Chatbots, Enterprise RAG	ark.cn-beijing.volces.com, /chat/completions, volces.com
SAP AI Core	https://community.sap.com/t5/technology-blogs-by-sap/ci-cd-with-sap-ai-core/ba-p/13708965	api.ai.prod.eu-central-1.aws.ml.hana.ondemand.com	OAuth2 (Client Creds)	POST /v2/inference/deployments/{id}/invocations	inputs, configuration	ai_core_client.deployment.create()	Enterprise ML Inference, Business Process AI	ml.hana.ondemand.com, /v2/inference
Riskified	https://www.riskified.com	wh.riskified.com	Basic Auth (Auth Token)	POST /api/decide, POST /api/checkout_create	order, customer, payment_details	riskified.decide()	Fraud Detection AI, Chargeback Guarantee	wh.riskified.com, /api/decide
Akismet	https://akismet.com	rest.akismet.com	API Key (Body param)	POST /1.1/comment-check	blog, user_ip, comment_content, comment_author	akismet.comment_check()	Spam Detection, Content Moderation	rest.akismet.com, /comment-check
Mapbox AI	https://www.mapbox.com/mapgpt	api.mapbox.com	Access Token (Query param)	GET /geocoding/v5/mapbox.places/{query}.json	types, proximity, fuzzyMatch	mapbox.geocoding.forward()	AI-Enhanced Search, Vision Navigation	api.mapbox.com, /geocoding/v5
PixVerse	https://pixverse.ai	app.pixverse.ai	Bearer Token (Web Internal)	POST /api/video/generate, GET /api/video/{id}	prompt, style_id, aspect_ratio	N/A (Web/Internal)	AI Video Generation	app.pixverse.ai, /api/video
xAI Grok API	https://grok.x.ai	api.x.ai	API Key (Header: Authorization: Bearer)	POST /v1/chat/completions	model (grok-2), messages, stream, temperature	client.chat.completions.create()	Real-time Reasoning, Tweet Analysis, Coding	api.x.ai, /v1/chat/completions, x-ai-token
Wolfram Alpha LLM API	https://www.wolframalpha.com	www.wolframalpha.com	API Key (Query param: appid)	GET /api/v1/llm-api	input, appid, maxchars	requests.get()	Computational Knowledge, Math Grounding for LLMs	wolframalpha.com, /api/v1/llm-api, appid=
Nuance Mix (Microsoft)	https://www.nuance.com	api.nuance.com	OAuth2 (Header: Authorization: Bearer)	POST /v4/conversational/recognize, POST /v4/tts/synthesize	audio, text, voice_model	mix_client.recognize()	Enterprise Speech Recognition, Biometrics	api.nuance.com, /v4/conversational, /v4/tts
LanguageTool API	https://languagetool.org	api.languagetool.org	API Key (Body: apiKey)	POST /v2/check	text, language, enabledOnly	requests.post()	Grammar Checking, Style Correction	api.languagetool.org, /v2/check
Runway API	https://runwayml.com	api.runwayml.com	API Key (Header: Authorization: Bearer)	POST /v1/image_to_video, GET /v1/tasks/{id}	image, prompt, duration, ratio	client.image_to_video.create()	Cinematic Video Generation, Gen-3 Alpha	api.runwayml.com, /v1/image_to_video
Agora AI	https://agora.io	api.agora.io	App ID / Token	POST /v1/projects/{appid}/cloud-recording/acquire	uid, cname, clientRequest	agora_client.start_recording()	Real-time Audio Transcription, Translation	api.agora.io, /cloud-recording
Sendbird AI	https://sendbird.com	api-{app_id}.sendbird.com	API Token (Header: Api-Token)	POST /v3/bots, POST /v3/group_channels/{url}/messages	bot_userid, message, ai_attribute	sb.GroupChannel.sendUserMessage()	In-app Chatbots, Summarization	sendbird.com, /v3/bots
Pictory AI	https://pictory.ai	api.pictory.ai	API Key (Header: Authorization)	POST /api/v1/video/storyboard, POST /api/v1/video/render	script, audio_settings, scenes	requests.post()	Text-to-Video, Marketing Clips	api.pictory.ai, /video/storyboard
Copyleaks API	https://copyleaks.com	api.copyleaks.com	Bearer Token (Header: Authorization)	POST /v3/scans/submit/file, POST /v3/ai-detection/submit/text	base64_file, text, properties	copyleaks.submit()	Plagiarism Detection, AI Content Detection	api.copyleaks.com, /v3/scans, /v3/ai-detection
Opus Clip	https://www.opus.pro	api.opus.pro	API Key (Header: X-API-Key)	POST /v1/clips/create	video_url, template_id	requests.post()	Short-form Video Repurposing, Virality AI	api.opus.pro, /v1/clips
Happy Scribe	https://happyscribe.com	api.happyscribe.com	API Key (Header: Authorization: Bearer)	POST /v1/transcriptions, POST /v1/exports	audio_url, language, format	requests.post()	Transcription, Subtitling	api.happyscribe.com, /v1/transcriptions
Dezgo	https://dezgo.sjv.io	api.dezgo.com	API Key (Header: X-Dezgo-Key)	POST /text2image, POST /image2image	prompt, model, upscale	requests.post()	Stable Diffusion Hosting, Image Gen	api.dezgo.com, /text2image
Meshy API	https://app.meshy.ai	api.meshy.ai	API Key (Header: Authorization: Bearer)	POST /v1/image-to-3d, POST /v1/text-to-3d	image_url, prompt, mode	meshy.create_task()	3D Asset Generation	api.meshy.ai, /v1/image-to-3d
Skywork AI	https://skywork.ai	api.skywork.cn	API Key (Header: Authorization)	POST /v1/chat/completions	model (skywork-13b), messages	client.chat.completions.create()	Chinese LLM, Enterprise Reasoning	api.skywork.cn, /v1/chat/completions
Wan Video	https://wan.video	wan.video	Bearer Token (Web Internal)	POST /api/generate	prompt, image, aspect_ratio	N/A (Web/Internal)	Video Generation	wan.video/api/generate
PixelBin (Watermark/Upscale)	https://www.watermarkremover.io	api.pixelbin.io	API Key (Header: Authorization)	POST /v2/transform/file	image, transformation (remove_bg/upscale)	pixelbin.transform()	Image Transformations, Watermark Removal	api.pixelbin.io, /v2/transform
Leonardo.Ai	https://leonardo.ai	cloud.leonardo.ai	API Key (Header: Authorization: Bearer)	POST /api/rest/v1/generations, GET /api/rest/v1/generations/{id}, POST /api/rest/v1/models	prompt, modelId, width, height, num_images, alchemy, photoReal	leonardo.generation.create_generation(), leonardo.generation.get_generation()	AI Art, Game Asset Design, Custom LoRA Training	cloud.leonardo.ai, /api/rest/v1/generations, Authorization: Bearer
SnapEdit	https://snapedit.app	api.snapedit.app	Bearer Token (Web Internal)	POST /api/v1/remove_object	image, mask, strategy	N/A (Web/Internal)	Object Removal, Photo Cleanup	api.snapedit.app, /remove_object
Meitu AI	https://www.meitu.com	openapi.mtlab.meitu.com	API Key / Sig	POST /v1/image/segmentation, POST /v1/image/enhancement	media_info, parameter	requests.post()	Face Beautification, Anime Filters	openapi.mtlab.meitu.com, /v1/image
Artguru	https://www.artguru.ai	artguru.ai	Bearer Token (Web Internal)	POST /api/generate_art	prompt, style_id	N/A (Web/Internal)	Avatar Generation, Face Swap	artguru.ai/api
TopMediai	https://topmediai.com	api.topmediai.com	API Key (Header: x-api-key)	POST /v1/tts, POST /v1/voice_clone	text, speaker_id, file	requests.post()	Voice Cloning, Text to Speech	api.topmediai.com, /v1/tts
Imagetotext.info	https://www.imagetotext.info	www.imagetotext.info	None (Form Data)	POST /upload	file, language	N/A (Web/Internal)	OCR (Optical Character Recognition)	imagetotext.info/upload
Magic Hour	https://magichour.ai	api.magichour.ai	Bearer Token (Web Internal)	POST /api/v1/video/generate	prompt, style, length	N/A (Web/Internal)	Video Generation, Deepfake	api.magichour.ai, /video/generate
Narakeet	https://narakeet.com	api.narakeet.com	API Key (Header: x-api-key)	POST /text-to-speech/mp3	text, voice, speed	requests.post()	Text to Speech (Slideshows)	api.narakeet.com, /text-to-speech
Paraphraser.io	https://www.paraphraser.io	www.paraphraser.io	API Key (Header: APIKEY)	POST /api/paraphrase	text, mode, lang	requests.post()	Text Rewriting, Spinning	paraphraser.io/api/paraphrase
AI Novelist	https://ai-novel.com	api.ai-novel.com	Bearer Token (Web Internal)	POST /v1/novel/generate	context, length, style	N/A (Web/Internal)	Japanese Novel Generation	api.ai-novel.com, /novel/generate
Anyclip	https://anyclip.com	api.anyclip.com	API Key	POST /v1/search/videos	query, limit, filters	requests.post()	Video Search, Contextual Targeting	api.anyclip.com, /search/videos
Alibaba Bailian (Model Studio)	https://bailian.console.alibabacloud.com	bailian.aliyuncs.com	API Key (Authorization: Bearer)	POST /api/v1/apps/{app_id}/completion	prompt, session_id, parameters	bailian.Completion.create()	Enterprise Agent Orchestration (Qwen)	bailian.aliyuncs.com, /api/v1/apps
Huawei Cloud (Pangu)	https://www.huaweicloud.com	iam.myhuaweicloud.com	IAM Token (X-Auth-Token)	POST /v1/{project_id}/pangu/chat/completions	messages, model_id	huaweicloud_sdk.pangu()	Enterprise LLM (Pangu), Weather/Drug Models	myhuaweicloud.com, /pangu/chat
ImageKit AI	https://imagekit.io	api.imagekit.io	API Key (Basic Auth)	POST /v1/files/upload (with AI tags)	file, extensions={"google-auto-tagging": true}	imagekit.upload()	Content-Aware Cropping, Auto-Tagging	api.imagekit.io, /v1/files/upload
TinEye	https://tineye.com	api.tineye.com	API Key (Header)	POST /search	image_url, limit	requests.post()	Reverse Image Search, Computer Vision	api.tineye.com, /search
Weglot	https://www.weglot.com	api.weglot.com	API Key (Query: api_key)	POST /translate	l_from, l_to, words	weglot.translate()	Website Localization, Neural Translation	api.weglot.com, /translate
LALAL.AI	https://www.lalal.ai	www.lalal.ai	API Key (Header: Authorization: key)	POST /api/v2/split	input_file, stem	requests.post()	Stem Separation (Vocals/Drums)	www.lalal.ai/api, /v2/split
GigaChat (Sber)	https://developers.sber.ru/portal/products/gigachat	gigachat.devices.sberbank.ru	Cert/Token (Basic+Bearer)	POST /api/v1/chat/completions	model (GigaChat), messages	client.chat()	Russian LLM, Multimodal	gigachat.devices.sberbank.ru, /chat/completions
Perfect Corp	https://www.perfectcorp.com	api.perfectcorp.com	API Key (Header: X-API-Key)	POST /v1/makeup/apply, POST /v1/skincare/analyze	image_base64, makeup_id	requests.post()	Virtual Try-On, Skin Analysis	api.perfectcorp.com, /v1/makeup
Rev AI	https://www.rev.com	api.rev.ai	API Key (Header: Authorization: Bearer)	POST /speechtotext/v1/jobs	media_url, metadata	rev_ai.submit_job()	High-Accuracy Transcription	api.rev.ai, /speechtotext
Replit	https://replit.com	replit.com	Bearer Token (Web Internal)	POST /graphql (Operation: CompleteCode)	query, prompt, context	N/A (Web/Internal)	Code Autocomplete (Ghostwriter)	replit.com/graphql, CompleteCode
Gamma App	https://gamma.app	gamma.app	Bearer Token (Web Internal)	POST /api/decks/create	topic, theme_id	N/A (Web/Internal)	AI Presentation Generation	gamma.app/api/decks
Miro AI	https://miro.com	api.miro.com	OAuth2	POST /v2/boards/{id}/items (with AI prompt)	content, side	client.create_sticky_note()	Visual Thinking, Mind Map Gen	api.miro.com/v2"

localAI:"Tool Name	URL	Base Domain	Payload Parameters	SDK Function Calls	Use Cases	Network Fingerprints	Category
TensorFlow.js	https://js.tensorflow.org/api/latest/	js.tensorflow.org	model URL or file, input tensors, batch_size, dtype	tf.loadLayersModel(), model.predict(), tf.browser.fromPixels()	On-device inference, image classification, in-browser training	/model/model.json, *.bin shards, cdn.jsdelivr.net/npm/@tensorflow, IndexedDB keys (tfjs-models)	Runtime (JS)
ONNX Runtime Web	https://onnxruntime.ai/docs/tutorials/web/	onnxruntime.ai	model.onnx path, input tensors, executionProviders (wasm/webgl)	InferenceSession.create(), session.run()	Transformer/CV inference in browser, ONNX model execution	*.onnx, ort-wasm.wasm, /wasm/, CDN hosts (unpkg, jsdelivr), IndexedDB keys	Runtime (Web)
WebLLM	https://webllm.mlc.ai	webllm.mlc.ai	model file (gguf/safetensors), prompt, max_tokens, temperature, streaming API	loadModel(), generate(), loadTokenizer()	On-device LLM chat, offline RAG, personal assistants	*.gguf, *.safetensors, webllm.wasm, chunked model fetch URLs, IndexedDB model cache	Runtime (LLM/web)
Transformers.js	https://huggingface.co/docs/transformers.js/en/index	huggingface.co	model id, input/inputs, max_length, top_k, temperature	pipeline(), AutoModel.from_pretrained(), tokenizer.encode()	Browser transformer inference, small LLMs, text generation	/models/{id}/config.json, .bin shards, huggingface.co CDN, wasm files	Library (TF/HF in browser)
MediaPipe	https://mediapipe.google.com	mediapipe.google.com	input stream (camera), options, model files	GraphRunner.start(), Hands.send(), FaceMesh.process()	On-device CV: hand tracking, pose, face landmarking	*.tflite, mediapipe wasm, /modules/, CDN-hosted models	Framework (CV)
PyScript	https://pyscript.net	pyscript.net	python source, package list, mount FS	loadPyodide(), pyscript.run(), pyodide.runPython()	Browser Python apps, on-device data processing, prototypes	pyodide.wasm, packages from pypi/cdn (pyodide-cdn.org), IndexedDB package caches	Framework (WASM Python)
Pyodide	https://pyodide.org/en/stable/	pyodide.org	python code, packages, FS mounts	pyodide.loadPackage(), pyodide.runPython()	WASM Python runtime, scientific stack in-browser	pyodide.wasm, .data files, pypi package fetches, CDN caches	Framework (WASM Python)
Burn	https://crates.io/crates/burn	crates.io	model binary, tensor buffers, config	wasm exports (init, infer), Rust function bindings	Embedded/WASM DL, rust-native inference	build/*.wasm, model.onnx/.tflite conversions, Cargo crates	Framework (Rust/WASM)
Dawn	https://dawn.googlesource.com/dawn	dawn.googlesource.com	device descriptors, shader modules	device.requestAdapter(), device.createShaderModule()	WebGPU implementation for local compute	dawn native libs, shader SPIR-V, browser integration artifacts	Framework (WebGPU impl)
Firefox AI Runtime	https://firefox-source-docs.mozilla.org/toolkit/components/ml	firefox-source-docs.mozilla.org	model file, input tensors, feature flags	moz.runInference(), FirefoxModel.run()	Browser-integrated local inference (privacy features)	firefox nightly flags, internal wasm/model paths, about:config flags	Framework (browser runtime)
Chrome Built-in AI	https://www.built-in-ai.dev/docs/ai-sdk-v6	built-in-ai.dev	ai.runModel(modelHandle, inputs), model import endpoints	builtInAI.loadModel(), builtInAI.query()	Chrome experimental on-device assistant, local SDK	model blobs, chrome://flags, built-in model stores, browser telemetry endpoints (if enabled)	Framework / SDK (browser built-in)
Brain.js	https://brain.js.org	brain.js.org	input arrays, training JSON, options	new brain.NeuralNetwork(), net.run(), net.train()	Simple neural networks in JS, demos, small classification	network JSON, model.export(), localStorage keys	Library
ml5.js	https://ml5.js.org	ml5js.org	image/audio input, model URL, options	ml5.imageClassifier(), classifier.classify()	Educational ML, quick demos, creative coding	/model/model.json, cdn.jsdelivr.net, ml5 model caches	Library
ConvNetJS	https://cs.stanford.edu/people/karpathy/convnetjs	karpathy.github.io	net definitions JSON, input vectors, trainer params	new convnetjs.Net(), net.forward(), trainer.train()	Historic in-browser NN experiments, teaching	network JSON files, localStorage training state	Library
Synaptic.js	https://caza.la/synaptic	caza.la	structure JSON, inputs, learning rate	new synaptic.Network(), network.activate()	Small networks, experiments, toy projects	network JSON, model export/import files	Library
Volver.js	https://volverjs.github.io/ai	volverjs.github.io	model URL, worker messages, chunk sizes	startWorker(), sendToWorker()	Transformers in web workers, UI isolation	worker.js, model shards, /transformers/, webworker fetches	Library (worker wrapper)
LLM.js	https://rahuldshetty.github.io/llm.js	rahuldshetty.github.io	model file (gguf/bin), prompt, max_tokens, streaming	loadLLM(), generate(), tokenizer.encode()	Small quantized LLMs in browser, local chat	*.gguf, tokenizer files, wasm backends, IndexedDB storage	Library
TypeGPU	https://docs.swmansion.com/TypeGPU	typegpu.docs.swmansion.com	shader code, buffers, layouts	device.createBuffer(), queue.submit()	WebGPU compute for ML ops, typed GPU bindings	.spv/.wgsl shaders, webgpu adapter queries	Library
OpenCV.js	https://opencv.org	opencv.org	image mats, cascade xml, params	cv.imread(), cv.imshow(), cv.CascadeClassifier.detectMultiScale()	CV operations, image processing in-browser	opencv.js, cascade xml, wasm files	Library
web-sys	https://docs.rs/web-sys/latest/web_sys	docs.rs	JS API calls, Request/Response objects	web_sys::window, web_sys::Request	Rust bindings to web APIs, enabling local ML runtimes in Rust	wasm-bindgen artifacts, .wasm, fetch calls	Library
Tree-sitter	https://tree-sitter.github.io/tree-sitter	tree-sitter.github.io	grammar, source code, language object	Parser.new(), parser.parse()	Code parsing in-browser (WASM), editor features	*.wasm grammar files, tree-sitter.wasm	Library
jsqr	https://cdn.jsdelivr.net/npm/jsqr@1.4.0/dist/jsQR.js	cdn.jsdelivr.net	imageData, width, height	jsQR()	QR code scanning in JS	CDN script (jsdelivr), jsQR.js, index.d.ts	Library
@built-in-ai/core	https://www.npmjs.com/package/@built-in-ai/core	npmjs.com	model handle, inputs, options	builtInAI.loadModel(), builtInAI.invoke()	Local browser-native AI SDK wrapper, provider shim	model blobs, chrome/edge builtin endpoints (internal)	Library / SDK
Brain4j	https://brain4j.org	brain4j.org	model JSON, data arrays	Network.create(), network.train()	Experimental JS/Java NN library, research prototypes	model export JSON	Library
AI Agent Toolkit	https://manus.im/en/tools	manus.im	agent config, tools, memory hooks	Agent.create(), agent.step(), agent.run()	Local agent orchestration, multi-tool agent prototypes	agent config fetches, tool scripts	Library / Tool
Window.ai	https://danduh.github.io/window-ai	danduh.github.io	model url, inputs, cache options	window.ai.loadModel(), window.ai.query()	Manage & run local models via extension	extension storage keys, local files, extension fetches	Tool (extension)
ChattyUI	https://chattyui.com	chattyui.com	props: messages, persona, modelHandle	ChatWidget.render(), ChatWidget.send()	UI layer for local chats	No external network by default; CDN script	Tool
Llama-UI.js	https://llama-ui.js.org	llama-ui.js.org	model path, prompt, options	llamaUI.init(), llamaUI.generate()	Local LLM front-ends, demos	*.gguf, model shards, wasm frontends	Tool / App
LocalAI_Analyzer	https://bangrui95.github.io/LocalAI_Analyzer	bangrui95.github.io	model path, analysis params	analyzer.run(), analyzer.report()	Model introspection, metadata extraction	model files, analyzer wasm	Tool
Crawllama	https://arn-c0de.github.io/Crawllama	arn-c0de.github.io	urls, selectors, depth	crawl(), parse()	Local web scraping in-browser, privacy-first crawling	fetch logs, crawl cache	Tool
ImgCompress	https://karimz1.github.io/imgcompress/installation	karimz1.github.io	file blob, quality, maxWidth	compress(), resize()	Client-side image compression, upload optimization	no external by default; file blobs, worker scripts	Tool
PlayCanvas (WebGPU guide)	https://blog.playcanvas.com/build-webgpu-apps-today-with-playcanvas/	blog.playcanvas.com	asset URLs, scene JSON, scripts	app.create(), app.assets.load(), app.start()	Game engine with WebGPU support	asset CDN, scene JSON, worker assets	Tool (engine)
Babylon.js (WebGPU support)	https://doc.babylonjs.com/setup/support/webGPU	babylonjs.com	scene files, assets, materials	Engine.runRenderLoop(), SceneLoader.Append()	3D and WebGPU compute assets	assets, .gltf/.babylon files, CDN modules	Tool (engine)
Three.js examples	https://threejs.org/examples/	threejs.org	scene/asset URLs, geometry, materials	GLTFLoader.load(), renderer.render()	3D rendering, WebGL/WebGPU experiments	.gltf, textures, CDN scripts	Tool (3D lib)
Multimind	https://www.multimind.dev	multimind.dev	agent config, tools, prompt history	multimind.build(), run()	Agent creation toolkits, local orchestrators	tool scripts, model fetches if connectors used	Tool / Platform
WebAssembly (WASM)	https://webassembly.org	webassembly.org	wasm path, imports, memory	WebAssembly.instantiate(), WebAssembly.instantiateStreaming()	Binary runtime for local models/accelerators	*.wasm, .wat, wasm module fetches	Standard
WebGPU (spec & repos)	https://github.com/gpuweb/gpuweb	github.com/gpuweb	adapter options, device descriptors	device.requestAdapter(), device.requestDevice()	GPU compute for ML kernels, local acceleration	webgpu adapter queries, shader modules (.wgsl)	Standard
WebGL (Khronos wiki)	https://www.khronos.org/webgl/wiki/Main_Page	khronos.org	shader sources, buffers, textures	gl.shaderSource(), gl.drawElements()	Graphics and GPGPU via fragment shaders	shader files, gl contexts	Standard
WebNN (Web ML intro)	https://webmachinelearning.github.io/webnn-intro	webmachinelearning.github.io	tensors, operations, descriptors	modelBuilder.add(), model.compute()	Hardware-accelerated NN ops via WebNN	device backend queries, model blobs	Standard
Model Context Protocol	https://modelcontextprotocol.io/introduction	modelcontextprotocol.io	payload schema, model id, dataset descriptors	mcp.connect(), mcp.query()	Connect models to data with standardized metadata	MCP manifests, connector endpoints (local)	Standard
Emscripten	https://emscripten.org	emscripten.org	compiled wasm, preloaded files, file system mounts	Module.cwrap(), FS.mount()	Compile C/C++ to WASM for local ML runtimes	*.wasm, .js glue code, preloaded data	Standard
WebChatAI (demo)	https://webbchatai.netlify.app	webbchatai.netlify.app	model path, prompt, conversation state	chat.init(), chat.ask()	Local chat demo, POC	model file fetches, demo assets	Demo
ML-Agents Bicycle (demo)	https://lukehollis.github.io/three-mlagents/bicycle	lukehollis.github.io	simulation state, action vector	env.reset(), agent.step()	Reinforcement learning demos in browser	audio/asset fetches, model files	Demo
Gemma Chat (Transformers.js demo)	https://1kaiser.github.io/gemma-chat-app	1kaiser.github.io	prompt, model id, options	pipeline('text-generation'), generate()	Gemma small LLM demo on WebGPU	/gemma/model files, transformers wasm, huggingface model shards	Demo
Brain.js Visual Editor	https://pwrmind.github.io/MLVisualEditor	pwrmind.github.io	editor inputs, net config, training data	editor.createNetwork(), exportJSON()	Visual NN builder, teaching	network JSON saves, localStorage	Demo
DeepSeek Browser Playground	https://ai-playground-browser-deepseek.sistemica.cloud	sistemica.cloud	model id, prompt, settings	playground.run(), generate()	Browser-based DeepSeek execution, demos	model files, wasm backends	Demo
WebPizza AI POC	https://webpizza-ai-poc.vercel.app	webpizza-ai-poc.vercel.app	model url, prompt, options	poc.loadModel(), poc.infer()	POC for local RAG/chat (browser-only)	model fetches, demo assets	Demo
Free Scribe Alpha	https://free-scribe-alpha.vercel.app	free-scribe-alpha.vercel.app	audio blob, language, config	transcribe(), loadModel()	Client-side speech-to-text demo	wasm STT, model files, audio blobs	Demo
Fully Local PDF Chatbot	https://fully-local-pdf-chatbot-topaz.vercel.app	topaz.vercel.app	PDF file blob, chunk size, embedding model	embed(), index(), query()	Local PDF RAG/chat, privacy-preserving RAG	embedding model files, IndexedDB RAG index	Demo
Fuji Web (experimental)	https://www.normalcomputing.com/blog/introducing-fuji-web	normalcomputing.com	prompts, model files	run functions, demo scripts	Experimental client-side AI platform	model fetches, demo assets	Demo / Blog
Genetic Cars (demo)	https://rednuht.org/genetic_cars_2	rednuht.org	simulation state, params	sim.step(), sim.mutate()	Evolutionary algorithm demo	no external by default; assets	Demo
Holobooth	https://holobooth.flutter.dev	holobooth.flutter.dev	image blob, settings	capture(), process()	Photobooth demo (Flutter/WASM), local effects	wasm plugins, model files	Demo
MNIST Digit Classifier	https://alanjoseph77.github.io/mnist-digit-classifier-js	alanjoseph77.github.io	model.json, image array, normalization	predict(), loadModel()	MNIST demo for classification	model.json, .bin shards	Demo
Stan Playground	https://flatironinstitute.github.io/stan-playground	flatironinstitute.github.io	model code, data, sampler params	runSampler(), compileModel()	Probabilistic programming in browser	wasm sampler, model data	Demo
Local Ideation Agent	https://piotrlaczkowski.github.io/WebGUIBased-local-IdeationAgent	piotrlaczkowski.github.io	tools config, prompt	agent.init(), agent.run()	Local ideation / brainstorming agent	model assets, agent config	Demo
Anaglyph (Transformers.js demo)	https://lostbeard.github.io/SpawnDev.BlazorJS.TransformersJS/AnaglyphImageDemo	lostbeard.github.io	image input, model paths, options	loadModel(), infer()	Depth estimation demo, image tasks	model shards, wasm	Demo
StreamingKokoroJS	https://rhulha.github.io/StreamingKokoroJS	rhulha.github.io	text input, voice params, streaming callbacks	loadTTS(), stream()	Client-side TTS demo, streaming audio	tts.wasm, voice model files	Demo
ML Sharp Web Viewer	https://kstonekuan.github.io/ml-sharp-web-viewer	kstonekuan.github.io	model path, visualization params	loadModel(), visualize()	Browser model viewer, inspect model metadata	model files, wasm backends	Demo
Bleep That Sh*t	https://neonwatty.github.io/bleep-that-shit	neonwatty.github.io	audio blob, censor rules, model	process(), init()	Client-side audio censoring, privacy-first	wasm model, audio blobs	Demo
Performance RNN (Magenta)	https://magenta.tensorflow.org/demos/performance_rnn/index.html	magenta.tensorflow.org	model.json, seed notes, steps	loadModel(), generate()	Music generation demo (Magenta.js)	model.json, .bin shards	Demo
Free Voice Reader	https://freevoicereader.com	freevoicereader.com	text, voice, speed	play(), init()	Text-to-speech demo, accessibility	tts wasm, voice files	Demo
Free Subtitle	https://free-subtitle-ai.yashchauhan.dev	free-subtitle-ai.yashchauhan.dev	audio blob, language, format	transcribe(), exportSRT()	Local transcription demo	wasm STT, model files	Demo
BrowserAI Docs/Demo	https://browserai.danduh.me	browserai.danduh.me	model files, prompts, options	initModel(), runPipeline()	Docs and demos for browser AI	model artifacts, demo assets	Demo
Web AI Chat (Takahirox)	https://takahirox.github.io/web_ai_chat/index.html	takahirox.github.io	prompt, context, modelPath	sendMessage(), loadModel()	Local chat demo, inference	model files, wasm	Demo
Browser Doc Parsing	https://browser-document-parsing-showcase.vercel.app	vercel.app	PDF/doc blob, parsing config	parse(), initParser()	Document parsing demo, local extraction	model wasm, parsing rules	Demo
WebNN MobileNet (Microsoft demo)	https://microsoft.github.io/webnn-developer-preview/demos/image-classification	microsoft.github.io	tensor input, ops descriptors, model graph	buildModel(), compute()	WebNN image classification demo	webnn model manifests, device backends	Demo
Mozilla Model Hub	https://model-hub.mozilla.org	model-hub.mozilla.org	download(), mirror()	Repo of local-optimized models, offline models	model archive URLs, mirror endpoints	Resource	Yes
TFLite Training Notebook (Colab)	https://colab.research.google.com/github/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/examples/on_device_training/overview.ipynb	colab.research.google.com	model code, training data, conversion flags	convert_to_tflite(), save()	On-device training resources, tutorials	.tflite, colab assets, cloud storage links (if used)	Resource
Firefox Local Alt Text (blog)	https://hacks.mozilla.org/2024/05/experimenting-with-local-alt-text-generation-in-firefox-nightly	hacks.mozilla.org	image blob, model, prompt	generateAltText(), loadModel()	Firefox experimental local alt text generation	model files, firefox-nightly flags	Resource
PyScript Blog (article)	https://www.marktechpost.com/2022/05/03/meet-pyscript-new-framework-from-anaconda-that-allows-users-to-create-rich-python-applications-in-the-browser-using-htmls-interface	marktechpost.com	scripts, package names, py-files	loadPyodide(), pyodide.runPython()	Article/resource about PyScript	pyodide.wasm, pypi fetches	Resource
Hugging Face (Gemma model page)	https://huggingface.co/google/gemma-3n-E2B-it-litert-preview	huggingface.co	hf_hub_download(), from_pretrained()	Model weights for local Gemma use	model shards, huggingface api paths, s3 mirror URLs	Resource	Yes
Kaggle Models (TFLite)	https://www.kaggle.com/models/google/gemma/tfLite	kaggle.com	artifact path, dataset id, file	tqdm download, save()	TFLite model repository .tflite files	.kaggle dataset artifacts, storage links	Resource
Fashion MNIST (dataset)	https://keras.io/api/datasets/fashion_mnist	keras.io	none (dataset arrays)	keras.datasets.fashion_mnist.load_data()	Dataset for demos and training	local dataset files, dataset URLs	Resource"

and ive been looking in to usecases of AI on the web as well.

like for example check this bit of content:"
Model
ThinkingThoughts
Expand to view model thoughts

chevron_right
Model
ThinkingThoughts
Expand to view model thoughts

chevron_right
Model
ThinkingThoughts
Expand to view model thoughts

chevron_right
Here are 2 advanced yet standardizable use cases for Vision (Computer Vision) and Microphone (Voice AI).
Crucial Crawler Note: To test "Microphone" or "Camera" features in a crawler (Playwright/Selenium), you must configure the browser context to allow permissions automatically, or the AI won't trigger.
Playwright config: permissions: ['microphone', 'camera']
Chrome flag: --use-fake-ui-for-media-stream (This feeds a fake test tone/image so the AI has something to process).
8. AI Background Removal (Computer Vision)
The Logic: "Image-In, Image-Out." The user uploads a photo, the browser sends it to an API, and the API returns a PNG with the background erased.
Target Site: remove.bg/upload
Where: The main "Upload Image" button.
How to Invoke (Standardized):
Method A (Hard): Use your crawler to upload a local file (setInputFiles).
Method B (Easy): Click one of the "Try one of these" sample images below the upload button. This triggers the exact same API call without needing a file system.
What to Watch (Network Tab):
Filter: xhr or removebg.
Observation: A POST request to api.remove.bg/v1.0/removebg.
Payload: Binary image data (or a URL reference).
Response: A JSON object containing the base64 string of the processed image, or a binary .png stream.
9. Real-Time Voice Agent (Audio/Microphone)
The Logic: A Conversational AI that listens to your voice via WebSocket, transcodes it (STT), processes LLM logic, and speaks back (TTS) instantly.
Target Site: vapi.ai
Where: The floating orb/character on the landing page (often labeled "Talk to Vapi" or "Call").
How to Invoke (Standardized):
Click the microphone/call icon.
Browser Prompt: The browser will ask for microphone permission (Your crawler must accept this automatically).
State Change: The icon usually turns into a "Listening" animation (waveform).
What to Watch (Network Tab):
Filter: WS (WebSocket).
Observation: A connection upgrade to wss://api.vapi.ai (or similar).
The Stream: Click the websocket entry and look at the Messages tab. You will see a flurry of JSON packets labeled audio-stream or transcript.
Why this is unique: Unlike chatbots (which wait for "Enter"), this AI sends data continuously 50 times a second while the mic is open.
Crawler Standardization Summary
For these "sensor" inputs, your crawler logic needs a specific "Permission & Asset" mode:
For Vision (Remove.bg):
Action: Locate selector div.sample-images > img -> Click.
Detection: Wait for POST response with content-type: image/* or application/json with base64 fields.
For Voice (Vapi):
Action: Grant microphone permission -> Click button[aria-label="microphone"].
Detection: Wait for WebSocket connection status 101 Switching Protocols.
info
Google AI models may make mistakes, so double-check outputs.
Use Arrow Up and Arrow Down to select a turn, Enter to jump to it, and Escape to return to the chat.
Start typing a prompt, use option + enter to append
google
Grounding with Google Search"

but my advisor wanted me to now pick pace up:"Feb 15, 2026 | AI on Web
Attendees: Yash Vekaria

Notes
Discussed progress on endpoints/function call metadata extraction for cloud + local AI
wapplyzer (nerdydata) 
https://github.com/duckduckgo/tracker-radar-collector

Action items
Complete local AI extraction (including the entry for resource URL – for downloading the service that provides AI)
Complete cloud AI extraction + structure for top 100k median tranco rank services, and add company name using fqdn/etld+1. develop more fine-grained sub-categorization. 
Usecase 1 – Chatbots: Study on research around chatbots detection and invoking, chatbot studies on webpages, regex, html tricks etc. heuristics from several papers to invoke+detect (merge these ideas), should work on all (majority + minority) websites. edge cases like a chatbot that first asks u questions (look into browser-use). interactions using ai like typing/clicking. crawler that invokes + captures network traffic etc
what information they are sending, to what endpoint, are they sending any prompt, what are they doing, what functions they are invoking/using (for other usecases as well). who is the “initiator” in devtools for conversation providers, for tracking endpoints (like for google analytics–gtm/gtag, who is integrating in first place), look into the js code
for services like hume and vapi ai, check out audio books websites or smthn and see what AI they use. 
focus on risks but the root might be linked to the sort of info being sent, network traffic, etc, personal info may be sent? maybe PII removed? how much chat being sent? history sent? third party (other orgs) + first party organizations (wrt ai provider)
work on usecases again taking into account these above ^"

so for this week's meeting, i need to do 3 things:

1. Usecase 1 – Chatbots: Study on research around chatbots detection and invoking, chatbot studies on webpages, regex, html tricks etc. heuristics from several papers to invoke+detect (merge these ideas), should work on all (majority + minority) websites. edge cases like a chatbot that first asks u questions (look into browser-use). interactions using ai like typing/clicking. crawler that invokes + captures network traffic etc
2. for the previous use cases i captured, i need to do a deep dive as to what information they are sending, to what endpoint, are they sending any prompt, what are they doing, what functions they are invoking/using (for other usecases as well). who is the “initiator” in devtools for conversation providers, for tracking endpoints (like for google analytics–gtm/gtag, who is integrating in first place), look into the js code
for services like hume and vapi ai, check out audio books websites or smthn and see what AI they use. 
focus on risks but the root might be linked to the sort of info being sent, network traffic, etc, personal info may be sent? maybe PII removed? how much chat being sent? history sent? third party (other orgs) + first party organizations (wrt ai provider)
and 3. start building the crawler, atleast the other essentials

now as for the crawler, the guidelines have been:"Methodology
Crawler
Crawl Tranco Top-1M webpages on the web using a modular crawler in language of choice.
Webpage content -> html + text
DOM of the page
Mainframe as well as iframes -> need both of these (dont simply loop since it might miss due to dynamic structure) -> might be linked to 3rd party orgs iframes
All network requests, responses, redirects, headers, payload, local storage/cookies?
Javascript files integrated for each frame
Perform interactions on a page
Accept all cookies on a webpage using/loading some extension such as Conset-O-Matic:
Set necessary consents by modifying values of variables D, A, B, E, F, and X to either true or false(default). The meaning of these variables are explained here. Set the values of these variables in the dictionary object: GDPRConfig.defaultValues present in the following file: /consent-extension/Consent-O-Matic/Extension/GDPRConfig.js
Perform bot-mitigation strategies to look like a real human
Random (human-like) mouse movements
Random clicks (on non-navigational portion/elements of the page)
Human-like scrolling until the bottom of the webpage and then go back to the top.
Random intervals of pause
Using stealth mode (as in playwright) or browser-use or undetected webdriver (as with selenium)
Performing crawls in headed mode and use relevant browser flags (if applicable)
UserAgent rotation (if needed)
at start when web opens we might have a timeout like 30s and separate external timeout for 2mins
Perform interactions to invoke AI on the webpage (if integrated)
Input “meaningful” text on all input/text/textbox or other similar elements, audio inputs, video inputs to trigger event listeners
First clicking on icons such as “Ask AI”, chatbot icon, “Summarize” button, etc. What else?
Triggering “Talk to AI” or similar feature (if available) by providing pre-stored voice input through microphone API or some alternative? CSPs
what permissions and how to accept
research on chatbots, capturing them, maybe some tool developed on github or so
Write a quick/simple chrome extension (with MV3) to be loaded along with the crawler or some similar approach to: 
Breakpoints or Code patching/overriding/hooking → for frame navigation or web request → 1) chrome.webrequest → chrome developers api, 2) cdp api:
CDP: https://chromedevtools.github.io/devtools-protocol/
main purpose was funtion overwriting (expensive for cloud, maybe could use for local, but open to exploration)
Capture stack traces of each network request (for each frame):
What function call (line number) of what script resulted in sending out of the network request?
Capture stack traces related to event listeners (usecase specific listeners capturing) specific to performed interactions pertaining to AI invocations (for each frame):
What interaction resulted in what function call (line number) of what script to be invoked?
What kind of objects, elements, etc can integrated AI interact with or collect through different APIs? (maybe looking at few samples of code will give an idea)
Example, content of the webpage maybe extracted and sent by the AI function along with the user query/prompt
Can we enumerate all such accesses and capture their usage by AI services?
need to think of inputs to check for privacy concerns, anything being stored in local storage, what content being sent alongside the input, pii related to the input
Identify and visit support/faq/help pages along with privacy policy texts for each website and repeat crawl?
"

i dont need to do the entire crawler right now but atleast the essential structure, things like capturing stuff, human movemenet etc etc everything

so i need to get started with buulding the crawler and make sure i understand stuff (by including comments)

now im at the stage that i need to get started with building the crawler.

now i want you to reiterate what i need to do for thhis week's meeting, and give me a very detailed prompt for the crawler thing that i will feed to antigravity to fully build the crawler

give me another prompt to use deep research to different LLMs for researching around chatbot detection etc, and maybe give a few keywords/phrasees i can put into google scholar to search those up myself

REPLY: This is a significant step forward. You are moving from Discovery (finding the tools) to Measurement (analyzing how they work in the wild).
Here is the breakdown of your tasks for the week, followed by the specific prompts you requested to execute them.
1. Reiteration of This Week's Goals
For your meeting, you need to complete the following:
Deep Dive into Chatbot Detection & Invocation:
Conduct a literature/code review to find heuristics (Regex, HTML structure, CSS selectors) to automatically detect chatbot widgets.
Solve edge cases: How to wake up a chatbot? How to handle "pre-chat forms" (e.g., "What is your name?" before the chat starts)?
Identify how to simulate "typing" and "clicking" to trigger AI processing.
Deep Forensic Analysis (Manual/Small Scale):
Take a few known AI integrations (like Hume, Vapi, or standard chatbots on sites like Audiobooks).
Manually inspect the Network Tab in DevTools.
Trace the Data: identifying the Payload (what is sent? PII? Chat history?), the Endpoint, and the Initiator (which JS script started the call?).
Risk Assessment: Note potential privacy leaks (e.g., is audio sent raw? is context sent without consent?).
Build the Crawler Skeleton (The "Antigravity" Build):
Initialize the modular Python + Playwright crawler.
Implement Bot Mitigation (Stealth, Human mouse/scroll).
Implement Consent Management (Consent-O-Matic integration).
Implement Data Capture (HTML, IFrames, Network Requests, and crucial CDP/Stack Trace capture).
2. The "Antigravity" Prompt (Building the Crawler)
Context: Feed this to your coding assistant (Cursor/Windsurf/Antigravity). It acts as a comprehensive Product Requirement Document (PRD) for the crawler.
Prompt:
code
Markdown
You are a Senior Software Engineer specializing in Web Measurement and Browser Automation. I need you to build the skeleton and core modules for a highly sophisticated, modular web crawler using **Python** and **Playwright (Async)**.

**Project Goal:**
To crawl the Tranco Top 1M websites to detect, invoke, and analyze integrated AI services (chatbots, copilots, etc.).

**Core Requirements:**
The crawler must be modular. Create a structure like `crawler/` with modules for `browser.py`, `interaction.py`, `capture.py`, `utils.py`.

**1. Browser Configuration (browser.py):**
*   Use `playwright-stealth` or standard stealth flags to avoid bot detection.
*   Launch in **HEADED** mode (required for some extensions/renderers) but manage window positioning so it doesn't block the user.
*   **Extension Loading:** We must load the "Consent-O-Matic" extension. Provide the logic to load an unpacked extension from a local path (`./extensions/Consent-O-Matic`).
*   **Timeouts:** Set a strict page load timeout (30s) but a longer interaction timeout (2min).

**2. Human-Like Interaction (interaction.py):**
*   Implement a function `simulate_human_behavior(page)`:
    *   **Mouse:** Move the mouse in random, non-linear Bezier curves (not straight lines) to random non-navigational elements.
    *   **Scroll:** Scroll down to the bottom and back up with random pauses, simulating reading.
    *   **Pauses:** Insert `random.uniform(1, 3)` waits between actions.

**3. Advanced Data Capture (capture.py) - CRITICAL:**
*   **Frame Handling:** We cannot just scrape the main frame. We must iterate through `page.frames` to capture content from IFrames (where chatbots often live).
*   **Content:** Capture HTML, inner text, and the DOM tree.
*   **Network Monitoring:** 
    *   Capture ALL requests/responses.
    *   Store: URL, Method, Headers, Payload (POST data), and Response Body.
*   **CDP / Stack Traces (The Hard Part):** 
    *   We need to know *who* initiated a request. 
    *   Use the Chrome DevTools Protocol (CDP) via `client = await page.context.new_cdp_session(page)`.
    *   Enable `Network` and `Debugger` domains.
    *   Listen for `Network.requestWillBeSent`.
    *   **Goal:** Capture the `initiator` field from the CDP event, specifically looking for the **Stack Trace** (Script URL + Line Number) that triggered the request.

**4. AI Invocation Logic (Skeleton only for now):**
*   Create a placeholder function `trigger_ai_components(page)`.
*   Logic: Find elements with aria-labels or text matching regex like `/(chat|ask|ai|bot|help)/i`.
*   Logic: Find input fields and simulate typing "meaningful" text (e.g., "Hello, can you summarize this page?").

**Output Format:**
The crawler should save data to a structured JSON log file per visit.

**Deliverables:**
Write the Python code for the directory structure and the specific modules described above. Ensure code is heavily commented to explain *why* we are doing things (e.g., "Using CDP to capture stack traces because standard Playwright logging misses the initiator script").
3. The Deep Research Prompt (For Chatbot Detection)
Context: Feed this to a reasoning model (o1, DeepSeek R1, or GPT-4o) to gather the heuristics you need for the "Usecase 1" task.
Prompt:
code
Markdown
I am conducting a web measurement study to automatically detect and interact with third-party AI Chatbots embedded on websites (e.g., Intercom, Drift, Tawk.to, or custom LLM widgets).

I need to perform a "Deep Research" dive into existing methodologies for **Chatbot Detection and Invocation** on the web.

**Your Task:**
1.  **Literature & Code Review:** Search for academic papers, GitHub repositories (e.g., OpenWPM, tracker-radar), or technical blog posts that discuss how to programmatically identify chat widgets.
2.  **Heuristics Generation:** Based on your research, compile a list of robust heuristics to detect these widgets. I am looking for:
    *   **Regex/Keywords:** Common terms in DOM elements (e.g., `id="intercom-container"`, `class="chat-widget"`).
    *   **DOM Structure:** How are they usually injected? (Shadow DOM? IFrames? Fixed positioning `z-index: 9999`?).
    *   **Initiator Scripts:** Common JS filenames (e.g., `widget.js`, `bundle.js`) associated with major providers.
3.  **Invocation Strategies:**
    *   How do we "wake up" a chatbot that is hidden behind a bubble icon?
    *   How do we handle "Pre-chat Forms" (where the bot asks for Name/Email before letting you type)? What are the strategies to bypass or fill these automatically?
4.  **Edge Cases:**
    *   How to distinguish a "Search Bar" from a "AI Chat Input"?
    *   How to handle chatbots inside Shadow DOMs?

**Output:**
Provide a structured report with concrete Regex patterns, CSS selectors, and logic flowcharts that I can translate into Python/Playwright code.
4. Google Scholar / Search Keywords
Use these specific queries to find relevant academic papers and technical write-ups:
"web measurement" third-party chatbot detection
automated detection of conversational agents on websites
privacy analysis of web chat widgets
programmatic interaction with web interfaces
OpenWPM chatbot detection
identifying third-party trackers web measurement (Chatbots are often classified as trackers in these studies)
UI element detection heuristics DOM analysis
automating interaction with cookie consent banners (Similar logic applies to pre-chat forms)
security risks of embedded chatbots