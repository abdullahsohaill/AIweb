# google.golang.org/genai
**URL:** https://pkg.go.dev/google.golang.org/genai
**Page Title:** genai package - google.golang.org/genai - Go Packages
--------------------


## README ¶

### Google Gen AI Go SDK

The Google Gen AI Go SDK provides an interface for developers to integrate
Google's generative models into their Go applications. It supports the Gemini Developer API and Vertex AI APIs.
[LINK: Gemini Developer API](https://ai.google.dev/gemini-api/docs)
[LINK: Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
The Google Gen AI Go SDK enables developers to use Google's state-of-the-art
generative AI models (like Gemini) to build AI-powered features and applications.
This SDK supports use cases like:
- Generate text from text-only input
- Generate text from text-and-images input (multimodal)
- ...
For example, with just a few lines of code, you can access Gemini's multimodal
capabilities to generate text from text-and-image input.
Add the SDK to your module with go get google.golang.org/genai .
You can create a client by configuring the necessary environment variables.
Configuration setup instructions depends on whether you're using the Gemini
Developer API or the Gemini API in Vertex AI.
Gemini Developer API: Set GOOGLE_API_KEY as shown below:
Gemini API on Vertex AI: Set GOOGLE_GENAI_USE_VERTEXAI , GOOGLE_CLOUD_PROJECT and GOOGLE_CLOUD_LOCATION , as shown below:
The contents of this repository are licensed under the Apache License, version 2.0 .

## Documentation ¶

### Index ¶

- Constants
- Variables
- func ConvertBidiSetupToTokenSetup(body map[string]any, config *CreateAuthTokenConfig) map[string]any
- func Ptr[T any](t T) *T
- func SetDefaultBaseURLs(baseURLParams BaseURLParameters)
- type APIAuth
[LINK: type APIAuth](#APIAuth)
- type APIAuthAPIKeyConfig
[LINK: type APIAuthAPIKeyConfig](#APIAuthAPIKeyConfig)
- type APIError
[LINK: type APIError](#APIError)
- func (e APIError) Error() string
- func (e APIError) Error() string
[LINK: func (e APIError) Error() string](#APIError.Error)
- type APIKeyConfig
[LINK: type APIKeyConfig](#APIKeyConfig)
- type APISpec
[LINK: type APISpec](#APISpec)
- type ActivityEnd
- type ActivityHandling
- type ActivityStart
- type AdapterSize
- type AudioTranscriptionConfig
- type AuthConfig
- type AuthConfigGoogleServiceAccountConfig
- type AuthConfigHTTPBasicAuthConfig
- type AuthConfigOauthConfig
- type AuthConfigOidcConfig
- type AuthToken
- type AuthType
- type AutomaticActivityDetection
- type Backend
- func (t Backend) String() string
- func (t Backend) String() string
- type BaseURLParameters
- type BatchJob
- func (b *BatchJob) MarshalJSON() ([]byte, error) func (b *BatchJob) UnmarshalJSON(data []byte) error
- func (b *BatchJob) MarshalJSON() ([]byte, error)
- func (b *BatchJob) UnmarshalJSON(data []byte) error
- type BatchJobDestination
- type BatchJobSource
- type Batches
- func (m Batches) All(ctx context.Context) iter.Seq2[*BatchJob, error] func (m Batches) Cancel(ctx context.Context, name string, config *CancelBatchJobConfig) error func (b Batches) Create(ctx context.Context, model string, src *BatchJobSource, ...) (*BatchJob, error) func (b Batches) CreateEmbeddings(ctx context.Context, model *string, src *EmbeddingsBatchJobSource, ...) (*BatchJob, error) func (m Batches) Delete(ctx context.Context, name string, config *DeleteBatchJobConfig) (*DeleteResourceJob, error) func (m Batches) Get(ctx context.Context, name string, config *GetBatchJobConfig) (*BatchJob, error) func (m Batches) List(ctx context.Context, config *ListBatchJobsConfig) (Page[BatchJob], error)
- func (m Batches) All(ctx context.Context) iter.Seq2[*BatchJob, error]
- func (m Batches) Cancel(ctx context.Context, name string, config *CancelBatchJobConfig) error
- func (b Batches) Create(ctx context.Context, model string, src *BatchJobSource, ...) (*BatchJob, error)
- func (b Batches) CreateEmbeddings(ctx context.Context, model *string, src *EmbeddingsBatchJobSource, ...) (*BatchJob, error)
- func (m Batches) Delete(ctx context.Context, name string, config *DeleteBatchJobConfig) (*DeleteResourceJob, error)
- func (m Batches) Get(ctx context.Context, name string, config *GetBatchJobConfig) (*BatchJob, error)
- func (m Batches) List(ctx context.Context, config *ListBatchJobsConfig) (Page[BatchJob], error)
- type Behavior
- type Blob
- type BlockedReason
- type CachedContent
- func (c *CachedContent) MarshalJSON() ([]byte, error) func (c *CachedContent) UnmarshalJSON(data []byte) error
- func (c *CachedContent) MarshalJSON() ([]byte, error)
- func (c *CachedContent) UnmarshalJSON(data []byte) error
- type CachedContentUsageMetadata
- type Caches
- func (m Caches) All(ctx context.Context) iter.Seq2[*CachedContent, error] func (m Caches) Create(ctx context.Context, model string, config *CreateCachedContentConfig) (*CachedContent, error) func (m Caches) Delete(ctx context.Context, name string, config *DeleteCachedContentConfig) (*DeleteCachedContentResponse, error) func (m Caches) Get(ctx context.Context, name string, config *GetCachedContentConfig) (*CachedContent, error) func (m Caches) List(ctx context.Context, config *ListCachedContentsConfig) (Page[CachedContent], error) func (m Caches) Update(ctx context.Context, name string, config *UpdateCachedContentConfig) (*CachedContent, error)
- func (m Caches) All(ctx context.Context) iter.Seq2[*CachedContent, error]
- func (m Caches) Create(ctx context.Context, model string, config *CreateCachedContentConfig) (*CachedContent, error)
- func (m Caches) Delete(ctx context.Context, name string, config *DeleteCachedContentConfig) (*DeleteCachedContentResponse, error)
- func (m Caches) Get(ctx context.Context, name string, config *GetCachedContentConfig) (*CachedContent, error)
- func (m Caches) List(ctx context.Context, config *ListCachedContentsConfig) (Page[CachedContent], error)
- func (m Caches) Update(ctx context.Context, name string, config *UpdateCachedContentConfig) (*CachedContent, error)
- type CancelBatchJobConfig
- type CancelTuningJobConfig
- type CancelTuningJobResponse
- type Candidate
- type Chat
- func (c *Chat) History(curated bool) []*Content func (c *Chat) Send(ctx context.Context, parts ...*Part) (*GenerateContentResponse, error) func (c *Chat) SendMessage(ctx context.Context, parts ...Part) (*GenerateContentResponse, error) func (c *Chat) SendMessageStream(ctx context.Context, parts ...Part) iter.Seq2[*GenerateContentResponse, error] func (c *Chat) SendStream(ctx context.Context, parts ...*Part) iter.Seq2[*GenerateContentResponse, error]
- func (c *Chat) History(curated bool) []*Content
- func (c *Chat) Send(ctx context.Context, parts ...*Part) (*GenerateContentResponse, error)
- func (c *Chat) SendMessage(ctx context.Context, parts ...Part) (*GenerateContentResponse, error)
- func (c *Chat) SendMessageStream(ctx context.Context, parts ...Part) iter.Seq2[*GenerateContentResponse, error]
- func (c *Chat) SendStream(ctx context.Context, parts ...*Part) iter.Seq2[*GenerateContentResponse, error]
- type Chats
- func (c *Chats) Create(ctx context.Context, model string, config *GenerateContentConfig, ...) (*Chat, error)
- func (c *Chats) Create(ctx context.Context, model string, config *GenerateContentConfig, ...) (*Chat, error)
- type Checkpoint
- type ChunkingConfig
- type Citation
- func (c *Citation) MarshalJSON() ([]byte, error) func (c *Citation) UnmarshalJSON(data []byte) error
- func (c *Citation) MarshalJSON() ([]byte, error)
- func (c *Citation) UnmarshalJSON(data []byte) error
- type CitationMetadata
- type Client
- func NewClient(ctx context.Context, cc *ClientConfig) (*Client, error)
- func NewClient(ctx context.Context, cc *ClientConfig) (*Client, error)
- func (c Client) ClientConfig() ClientConfig
- func (c Client) ClientConfig() ClientConfig
- type ClientConfig
- func (cc *ClientConfig) UseDefaultCredentials() error
- func (cc *ClientConfig) UseDefaultCredentials() error
- type CodeExecutionResult
- type CompletionStats
- type ComputeTokensConfig
- type ComputeTokensResponse
- type ComputeTokensResult
- type ComputerUse
- type Content
- func NewContentFromBytes(data []byte, mimeType string, role Role) *Content func NewContentFromCodeExecutionResult(outcome Outcome, output string, role Role) *Content func NewContentFromExecutableCode(code string, language Language, role Role) *Content func NewContentFromFunctionCall(name string, args map[string]any, role Role) *Content func NewContentFromFunctionResponse(name string, response map[string]any, role Role) *Content func NewContentFromParts(parts []*Part, role Role) *Content func NewContentFromText(text string, role Role) *Content func NewContentFromURI(fileURI, mimeType string, role Role) *Content func Text(text string) []*Content
- func NewContentFromBytes(data []byte, mimeType string, role Role) *Content
- func NewContentFromCodeExecutionResult(outcome Outcome, output string, role Role) *Content
- func NewContentFromExecutableCode(code string, language Language, role Role) *Content
- func NewContentFromFunctionCall(name string, args map[string]any, role Role) *Content
- func NewContentFromFunctionResponse(name string, response map[string]any, role Role) *Content
- func NewContentFromParts(parts []*Part, role Role) *Content
- func NewContentFromText(text string, role Role) *Content
- func NewContentFromURI(fileURI, mimeType string, role Role) *Content
- func Text(text string) []*Content
- type ContentEmbedding
- type ContentEmbeddingStatistics
- type ContentReferenceImage
- func NewContentReferenceImage(referenceImage *Image, referenceID int32) *ContentReferenceImage
- func NewContentReferenceImage(referenceImage *Image, referenceID int32) *ContentReferenceImage
- type ContextWindowCompressionConfig
- type ControlReferenceConfig
- type ControlReferenceImage
- func NewControlReferenceImage(referenceImage *Image, referenceID int32, config *ControlReferenceConfig) *ControlReferenceImage
- func NewControlReferenceImage(referenceImage *Image, referenceID int32, config *ControlReferenceConfig) *ControlReferenceImage
- type ControlReferenceType
- type CountTokensConfig
- type CountTokensResponse
- type CountTokensResult
- type CreateAuthTokenConfig
- func (c *CreateAuthTokenConfig) MarshalJSON() ([]byte, error) func (c *CreateAuthTokenConfig) UnmarshalJSON(data []byte) error
- func (c *CreateAuthTokenConfig) MarshalJSON() ([]byte, error)
- func (c *CreateAuthTokenConfig) UnmarshalJSON(data []byte) error
- type CreateBatchJobConfig
- type CreateCachedContentConfig
- func (c *CreateCachedContentConfig) MarshalJSON() ([]byte, error) func (c *CreateCachedContentConfig) UnmarshalJSON(data []byte) error
- func (c *CreateCachedContentConfig) MarshalJSON() ([]byte, error)
- func (c *CreateCachedContentConfig) UnmarshalJSON(data []byte) error
- type CreateEmbeddingsBatchJobConfig
- type CreateFileConfig
- type CreateFileResponse
- type CreateFileSearchStoreConfig
- type CreateTuningJobConfig
- type CustomMetadata
- type DatasetDistribution
- type DatasetDistributionDistributionBucket
- type DatasetStats
- type DeleteBatchJobConfig
- type DeleteCachedContentConfig
- type DeleteCachedContentResponse
- type DeleteDocumentConfig
- type DeleteFileConfig
- type DeleteFileResponse
- type DeleteFileSearchStoreConfig
- type DeleteModelConfig
- type DeleteModelResponse
- type DeleteResourceJob
- type DistillationDataStats
- type DistillationHyperParameters
- type DistillationSpec
- type Document
- func (d *Document) MarshalJSON() ([]byte, error) func (d *Document) UnmarshalJSON(data []byte) error
- func (d *Document) MarshalJSON() ([]byte, error)
- func (d *Document) UnmarshalJSON(data []byte) error
- type DocumentState
- type Documents
- func (m Documents) All(ctx context.Context, parent string) iter.Seq2[*Document, error] func (m Documents) Delete(ctx context.Context, name string, config *DeleteDocumentConfig) error func (m Documents) Get(ctx context.Context, name string, config *GetDocumentConfig) (*Document, error) func (m Documents) List(ctx context.Context, parent string, config *ListDocumentsConfig) (Page[Document], error)
- func (m Documents) All(ctx context.Context, parent string) iter.Seq2[*Document, error]
- func (m Documents) Delete(ctx context.Context, name string, config *DeleteDocumentConfig) error
- func (m Documents) Get(ctx context.Context, name string, config *GetDocumentConfig) (*Document, error)
- func (m Documents) List(ctx context.Context, parent string, config *ListDocumentsConfig) (Page[Document], error)
- type DownloadFileConfig
- type DownloadURI
- func NewDownloadURIFromFile(f *File) DownloadURI func NewDownloadURIFromGeneratedVideo(v *GeneratedVideo) DownloadURI func NewDownloadURIFromVideo(v *Video) DownloadURI
- func NewDownloadURIFromFile(f *File) DownloadURI
- func NewDownloadURIFromGeneratedVideo(v *GeneratedVideo) DownloadURI
- func NewDownloadURIFromVideo(v *Video) DownloadURI
- type DynamicRetrievalConfig
- type DynamicRetrievalConfigMode
- type EditImageConfig
- type EditImageResponse
- type EditMode
- type EmbedContentBatch
- type EmbedContentConfig
- type EmbedContentMetadata
- type EmbedContentResponse
- type EmbeddingsBatchJobSource
- type EncryptionSpec
- type EndSensitivity
- type Endpoint
- type EnterpriseWebSearch
- type EntityLabel
- type Environment
- type ExecutableCode
- type ExternalAPI
[LINK: type ExternalAPI](#ExternalAPI)
- type ExternalAPIElasticSearchParams
[LINK: type ExternalAPIElasticSearchParams](#ExternalAPIElasticSearchParams)
- type ExternalAPISimpleSearchParams
[LINK: type ExternalAPISimpleSearchParams](#ExternalAPISimpleSearchParams)
- type ExtrasRequestProvider
- type FeatureSelectionPreference
- type FetchPredictOperationConfig
- type File
- func (f *File) MarshalJSON() ([]byte, error) func (f *File) UnmarshalJSON(data []byte) error
- func (f *File) MarshalJSON() ([]byte, error)
- func (f *File) UnmarshalJSON(data []byte) error
- type FileData
- type FileSearch
- type FileSearchStore
- func (f *FileSearchStore) MarshalJSON() ([]byte, error) func (f *FileSearchStore) UnmarshalJSON(data []byte) error
- func (f *FileSearchStore) MarshalJSON() ([]byte, error)
- func (f *FileSearchStore) UnmarshalJSON(data []byte) error
- type FileSearchStores
- func (m FileSearchStores) All(ctx context.Context) iter.Seq2[*FileSearchStore, error] func (m FileSearchStores) Create(ctx context.Context, config *CreateFileSearchStoreConfig) (*FileSearchStore, error) func (m FileSearchStores) Delete(ctx context.Context, name string, config *DeleteFileSearchStoreConfig) error func (m FileSearchStores) Get(ctx context.Context, name string, config *GetFileSearchStoreConfig) (*FileSearchStore, error) func (m FileSearchStores) ImportFile(ctx context.Context, fileSearchStoreName string, fileName string, ...) (*ImportFileOperation, error) func (m FileSearchStores) List(ctx context.Context, config *ListFileSearchStoresConfig) (Page[FileSearchStore], error) func (m FileSearchStores) UploadToFileSearchStore(ctx context.Context, r io.Reader, FileSearchStoreName string, ...) (*UploadToFileSearchStoreOperation, error) func (m FileSearchStores) UploadToFileSearchStoreFromPath(ctx context.Context, path string, FileSearchStoreName string, ...) (*UploadToFileSearchStoreOperation, error)
- func (m FileSearchStores) All(ctx context.Context) iter.Seq2[*FileSearchStore, error]
- func (m FileSearchStores) Create(ctx context.Context, config *CreateFileSearchStoreConfig) (*FileSearchStore, error)
- func (m FileSearchStores) Delete(ctx context.Context, name string, config *DeleteFileSearchStoreConfig) error
- func (m FileSearchStores) Get(ctx context.Context, name string, config *GetFileSearchStoreConfig) (*FileSearchStore, error)
- func (m FileSearchStores) ImportFile(ctx context.Context, fileSearchStoreName string, fileName string, ...) (*ImportFileOperation, error)
- func (m FileSearchStores) List(ctx context.Context, config *ListFileSearchStoresConfig) (Page[FileSearchStore], error)
- func (m FileSearchStores) UploadToFileSearchStore(ctx context.Context, r io.Reader, FileSearchStoreName string, ...) (*UploadToFileSearchStoreOperation, error)
- func (m FileSearchStores) UploadToFileSearchStoreFromPath(ctx context.Context, path string, FileSearchStoreName string, ...) (*UploadToFileSearchStoreOperation, error)
- type FileSource
- type FileState
- type FileStatus
- type Files
- func (m Files) All(ctx context.Context) iter.Seq2[*File, error] func (m Files) Delete(ctx context.Context, name string, config *DeleteFileConfig) (*DeleteFileResponse, error) func (m Files) Download(ctx context.Context, uri DownloadURI, config *DownloadFileConfig) ([]byte, error) func (m Files) Get(ctx context.Context, name string, config *GetFileConfig) (*File, error) func (m Files) List(ctx context.Context, config *ListFilesConfig) (Page[File], error) func (m Files) Upload(ctx context.Context, r io.Reader, config *UploadFileConfig) (*File, error) func (m Files) UploadFromPath(ctx context.Context, path string, config *UploadFileConfig) (*File, error)
- func (m Files) All(ctx context.Context) iter.Seq2[*File, error]
- func (m Files) Delete(ctx context.Context, name string, config *DeleteFileConfig) (*DeleteFileResponse, error)
- func (m Files) Download(ctx context.Context, uri DownloadURI, config *DownloadFileConfig) ([]byte, error)
- func (m Files) Get(ctx context.Context, name string, config *GetFileConfig) (*File, error)
- func (m Files) List(ctx context.Context, config *ListFilesConfig) (Page[File], error)
- func (m Files) Upload(ctx context.Context, r io.Reader, config *UploadFileConfig) (*File, error)
- func (m Files) UploadFromPath(ctx context.Context, path string, config *UploadFileConfig) (*File, error)
- type FinishReason
- type FunctionCall
- type FunctionCallingConfig
- type FunctionCallingConfigMode
- type FunctionDeclaration
- type FunctionResponse
- type FunctionResponseBlob
- type FunctionResponseFileData
- type FunctionResponsePart
- func NewFunctionResponsePartFromBytes(data []byte, mimeType string) *FunctionResponsePart func NewFunctionResponsePartFromURI(fileURI, mimeType string) *FunctionResponsePart
- func NewFunctionResponsePartFromBytes(data []byte, mimeType string) *FunctionResponsePart
- func NewFunctionResponsePartFromURI(fileURI, mimeType string) *FunctionResponsePart
- type FunctionResponseScheduling
- type GeminiPreferenceExample
- type GeminiPreferenceExampleCompletion
- type GenerateContentConfig
- func (c GenerateContentConfig) ToGenerationConfig(backend Backend) (*GenerationConfig, error)
- func (c GenerateContentConfig) ToGenerationConfig(backend Backend) (*GenerationConfig, error)
- type GenerateContentResponse
- func (r *GenerateContentResponse) CodeExecutionResult() string func (r *GenerateContentResponse) ExecutableCode() string func (r *GenerateContentResponse) FunctionCalls() []*FunctionCall func (g *GenerateContentResponse) MarshalJSON() ([]byte, error) func (r *GenerateContentResponse) Text() string func (g *GenerateContentResponse) UnmarshalJSON(data []byte) error
- func (r *GenerateContentResponse) CodeExecutionResult() string
- func (r *GenerateContentResponse) ExecutableCode() string
- func (r *GenerateContentResponse) FunctionCalls() []*FunctionCall
- func (g *GenerateContentResponse) MarshalJSON() ([]byte, error)
- func (r *GenerateContentResponse) Text() string
- func (g *GenerateContentResponse) UnmarshalJSON(data []byte) error
- type GenerateContentResponsePromptFeedback
- type GenerateContentResponseUsageMetadata
- type GenerateImagesConfig
- type GenerateImagesResponse
- type GenerateVideosConfig
- type GenerateVideosOperation
- type GenerateVideosResponse
- type GenerateVideosSource
- type GeneratedImage
- type GeneratedImageMask
- type GeneratedVideo
- type GenerationConfig
- type GenerationConfigRoutingConfig
- type GenerationConfigRoutingConfigAutoRoutingMode
- type GenerationConfigRoutingConfigManualRoutingMode
- type GenerationConfigThinkingConfig
- type GetBatchJobConfig
- type GetCachedContentConfig
- type GetDocumentConfig
- type GetFileConfig
- type GetFileSearchStoreConfig
- type GetModelConfig
- type GetOperationConfig
- type GetTuningJobConfig
- type GoogleMaps
- type GoogleRpcStatus
- type GoogleSearch
- type GoogleSearchRetrieval
- type GroundingChunk
- type GroundingChunkMaps
- type GroundingChunkMapsPlaceAnswerSources
- type GroundingChunkMapsPlaceAnswerSourcesAuthorAttribution
- type GroundingChunkMapsPlaceAnswerSourcesReviewSnippet
- type GroundingChunkRetrievedContext
- type GroundingChunkWeb
- type GroundingMetadata
- type GroundingMetadataSourceFlaggingURI
- type GroundingSupport
- type HTTPElementLocation
- type HTTPOptions
- type HTTPResponse
- type HarmBlockMethod
- type HarmBlockThreshold
- type HarmCategory
- type HarmProbability
- type HarmSeverity
- type Image
- type ImageConfig
- type ImagePromptLanguage
- type ImportFileConfig
- type ImportFileOperation
- type ImportFileResponse
- type InlinedEmbedContentResponse
- type InlinedRequest
- type InlinedResponse
- type Interval
- func (i *Interval) MarshalJSON() ([]byte, error) func (i *Interval) UnmarshalJSON(data []byte) error
- func (i *Interval) MarshalJSON() ([]byte, error)
- func (i *Interval) UnmarshalJSON(data []byte) error
- type JobError
- type JobState
- type Language
- type LatLng
- type ListBatchJobsConfig
- type ListBatchJobsResponse
- type ListCachedContentsConfig
- type ListCachedContentsResponse
- type ListDocumentsConfig
- type ListDocumentsResponse
- type ListFileSearchStoresConfig
- type ListFileSearchStoresResponse
- type ListFilesConfig
- type ListFilesResponse
- type ListModelsConfig
- type ListModelsResponse
- type ListTuningJobsConfig
- type ListTuningJobsResponse
- type Live
- func (r *Live) Connect(context context.Context, model string, config *LiveConnectConfig) (*Session, error)
- func (r *Live) Connect(context context.Context, model string, config *LiveConnectConfig) (*Session, error)
- type LiveClientContent
- type LiveClientContentInput
- type LiveClientMessage
- type LiveClientRealtimeInput
- type LiveClientSetup
- type LiveClientToolResponse
- type LiveConnectConfig
- type LiveConnectConstraints
- type LiveRealtimeInput
- type LiveSendClientContentParameters
- type LiveSendRealtimeInputParameters
- type LiveSendToolResponseParameters
- type LiveServerContent
- type LiveServerGoAway
- func (l *LiveServerGoAway) MarshalJSON() ([]byte, error) func (l *LiveServerGoAway) UnmarshalJSON(data []byte) error
- func (l *LiveServerGoAway) MarshalJSON() ([]byte, error)
- func (l *LiveServerGoAway) UnmarshalJSON(data []byte) error
- type LiveServerMessage
- type LiveServerSessionResumptionUpdate
- type LiveServerSetupComplete
- type LiveServerToolCall
- type LiveServerToolCallCancellation
- type LiveToolResponseInput
- type LogprobsResult
- type LogprobsResultCandidate
- type LogprobsResultTopCandidates
- type MaskReferenceConfig
- type MaskReferenceImage
- func NewMaskReferenceImage(referenceImage *Image, referenceID int32, config *MaskReferenceConfig) *MaskReferenceImage
- func NewMaskReferenceImage(referenceImage *Image, referenceID int32, config *MaskReferenceConfig) *MaskReferenceImage
- type MaskReferenceMode
- type MediaModality
- type MediaResolution
- type Modality
- type ModalityTokenCount
- type Model
- type ModelArmorConfig
- type ModelSelectionConfig
- type Models
- func (m Models) All(ctx context.Context) iter.Seq2[*Model, error] func (m Models) ComputeTokens(ctx context.Context, model string, contents []*Content, ...) (*ComputeTokensResponse, error) func (m Models) CountTokens(ctx context.Context, model string, contents []*Content, ...) (*CountTokensResponse, error) func (m Models) Delete(ctx context.Context, model string, config *DeleteModelConfig) (*DeleteModelResponse, error) func (m Models) EditImage(ctx context.Context, model, prompt string, referenceImages []ReferenceImage, ...) (*EditImageResponse, error) func (m Models) EmbedContent(ctx context.Context, model string, contents []*Content, ...) (*EmbedContentResponse, error) func (m Models) GenerateContent(ctx context.Context, model string, contents []*Content, ...) (*GenerateContentResponse, error) func (m Models) GenerateContentStream(ctx context.Context, model string, contents []*Content, ...) iter.Seq2[*GenerateContentResponse, error] func (m Models) GenerateImages(ctx context.Context, model string, prompt string, config *GenerateImagesConfig) (*GenerateImagesResponse, error) func (m Models) GenerateVideos(ctx context.Context, model string, prompt string, image *Image, ...) (*GenerateVideosOperation, error) func (m Models) GenerateVideosFromSource(ctx context.Context, model string, source *GenerateVideosSource, ...) (*GenerateVideosOperation, error) func (m Models) Get(ctx context.Context, model string, config *GetModelConfig) (*Model, error) func (m Models) List(ctx context.Context, config *ListModelsConfig) (Page[Model], error) func (m Models) RecontextImage(ctx context.Context, model string, source *RecontextImageSource, ...) (*RecontextImageResponse, error) func (m Models) SegmentImage(ctx context.Context, model string, source *SegmentImageSource, ...) (*SegmentImageResponse, error) func (m Models) Update(ctx context.Context, model string, config *UpdateModelConfig) (*Model, error) func (m Models) UpscaleImage(ctx context.Context, model string, image *Image, upscaleFactor string, ...) (*UpscaleImageResponse, error)
- func (m Models) All(ctx context.Context) iter.Seq2[*Model, error]
- func (m Models) ComputeTokens(ctx context.Context, model string, contents []*Content, ...) (*ComputeTokensResponse, error)
- func (m Models) CountTokens(ctx context.Context, model string, contents []*Content, ...) (*CountTokensResponse, error)
- func (m Models) Delete(ctx context.Context, model string, config *DeleteModelConfig) (*DeleteModelResponse, error)
- func (m Models) EditImage(ctx context.Context, model, prompt string, referenceImages []ReferenceImage, ...) (*EditImageResponse, error)
- func (m Models) EmbedContent(ctx context.Context, model string, contents []*Content, ...) (*EmbedContentResponse, error)
- func (m Models) GenerateContent(ctx context.Context, model string, contents []*Content, ...) (*GenerateContentResponse, error)
- func (m Models) GenerateContentStream(ctx context.Context, model string, contents []*Content, ...) iter.Seq2[*GenerateContentResponse, error]
- func (m Models) GenerateImages(ctx context.Context, model string, prompt string, config *GenerateImagesConfig) (*GenerateImagesResponse, error)
- func (m Models) GenerateVideos(ctx context.Context, model string, prompt string, image *Image, ...) (*GenerateVideosOperation, error)
- func (m Models) GenerateVideosFromSource(ctx context.Context, model string, source *GenerateVideosSource, ...) (*GenerateVideosOperation, error)
- func (m Models) Get(ctx context.Context, model string, config *GetModelConfig) (*Model, error)
- func (m Models) List(ctx context.Context, config *ListModelsConfig) (Page[Model], error)
- func (m Models) RecontextImage(ctx context.Context, model string, source *RecontextImageSource, ...) (*RecontextImageResponse, error)
- func (m Models) SegmentImage(ctx context.Context, model string, source *SegmentImageSource, ...) (*SegmentImageResponse, error)
- func (m Models) Update(ctx context.Context, model string, config *UpdateModelConfig) (*Model, error)
- func (m Models) UpscaleImage(ctx context.Context, model string, image *Image, upscaleFactor string, ...) (*UpscaleImageResponse, error)
- type MultiSpeakerVoiceConfig
- type Operations
- func (m Operations) GetImportFileOperation(ctx context.Context, operation *ImportFileOperation, ...) (*ImportFileOperation, error) func (m Operations) GetUploadToFileSearchStoreOperation(ctx context.Context, operation *UploadToFileSearchStoreOperation, ...) (*UploadToFileSearchStoreOperation, error) func (m Operations) GetVideosOperation(ctx context.Context, operation *GenerateVideosOperation, ...) (*GenerateVideosOperation, error)
- func (m Operations) GetImportFileOperation(ctx context.Context, operation *ImportFileOperation, ...) (*ImportFileOperation, error)
- func (m Operations) GetUploadToFileSearchStoreOperation(ctx context.Context, operation *UploadToFileSearchStoreOperation, ...) (*UploadToFileSearchStoreOperation, error)
- func (m Operations) GetVideosOperation(ctx context.Context, operation *GenerateVideosOperation, ...) (*GenerateVideosOperation, error)
- type Outcome
- type Page
- func (p Page[T]) Next(ctx context.Context) (Page[T], error)
- func (p Page[T]) Next(ctx context.Context) (Page[T], error)
- type Part
- func NewPartFromBytes(data []byte, mimeType string) *Part func NewPartFromCodeExecutionResult(outcome Outcome, output string) *Part func NewPartFromExecutableCode(code string, language Language) *Part func NewPartFromFile(file File) *Part func NewPartFromFunctionCall(name string, args map[string]any) *Part func NewPartFromFunctionResponse(name string, response map[string]any) *Part func NewPartFromFunctionResponseWithParts(name string, response map[string]any, parts []*FunctionResponsePart) *Part func NewPartFromText(text string) *Part func NewPartFromURI(fileURI, mimeType string) *Part
- func NewPartFromBytes(data []byte, mimeType string) *Part
- func NewPartFromCodeExecutionResult(outcome Outcome, output string) *Part
- func NewPartFromExecutableCode(code string, language Language) *Part
- func NewPartFromFile(file File) *Part
- func NewPartFromFunctionCall(name string, args map[string]any) *Part
- func NewPartFromFunctionResponse(name string, response map[string]any) *Part
- func NewPartFromFunctionResponseWithParts(name string, response map[string]any, parts []*FunctionResponsePart) *Part
- func NewPartFromText(text string) *Part
- func NewPartFromURI(fileURI, mimeType string) *Part
- type PartMediaResolution
- type PartMediaResolutionLevel
- type PartialArg
- type PartnerModelTuningSpec
- type PersonGeneration
- type PhishBlockThreshold
- type PreTunedModel
- type PrebuiltVoiceConfig
- type PreferenceOptimizationDataStats
- type PreferenceOptimizationHyperParameters
- type PreferenceOptimizationSpec
- type ProactivityConfig
- type ProductImage
- type RAGChunk
- type RAGChunkPageSpan
- type RAGRetrievalConfig
- type RAGRetrievalConfigFilter
- type RAGRetrievalConfigHybridSearch
- type RAGRetrievalConfigRanking
- type RAGRetrievalConfigRankingLlmRanker
- type RAGRetrievalConfigRankingRankService
- type RawReferenceImage
- func NewRawReferenceImage(referenceImage *Image, referenceID int32) *RawReferenceImage
- func NewRawReferenceImage(referenceImage *Image, referenceID int32) *RawReferenceImage
- type RealtimeInputConfig
- type RecontextImageConfig
- type RecontextImageResponse
- type RecontextImageSource
- type ReferenceImage
- type ReplicatedVoiceConfig
- type Retrieval
- type RetrievalConfig
- type RetrievalMetadata
- type Role
- type SafetyAttributes
- type SafetyFilterLevel
- type SafetyRating
- type SafetySetting
- type Schema
- type ScribbleImage
- type SearchEntryPoint
- type Segment
- type SegmentImageConfig
- type SegmentImageResponse
- type SegmentImageSource
- type SegmentMode
- type Session
- func (s *Session) Close() error func (s *Session) Receive() (*LiveServerMessage, error) func (s *Session) SendClientContent(input LiveClientContentInput) error func (s *Session) SendRealtimeInput(input LiveRealtimeInput) error func (s *Session) SendToolResponse(input LiveToolResponseInput) error
- func (s *Session) Close() error
- func (s *Session) Receive() (*LiveServerMessage, error)
- func (s *Session) SendClientContent(input LiveClientContentInput) error
- func (s *Session) SendRealtimeInput(input LiveRealtimeInput) error
- func (s *Session) SendToolResponse(input LiveToolResponseInput) error
- type SessionResumptionConfig
- type SingleEmbedContentResponse
- type SlidingWindow
- type SpeakerVoiceConfig
- type SpeechConfig
- type StartSensitivity
- type StringList
- type StyleReferenceConfig
- type StyleReferenceImage
- func NewStyleReferenceImage(referenceImage *Image, referenceID int32, config *StyleReferenceConfig) *StyleReferenceImage
- func NewStyleReferenceImage(referenceImage *Image, referenceID int32, config *StyleReferenceConfig) *StyleReferenceImage
- type SubjectReferenceConfig
- type SubjectReferenceImage
- func NewSubjectReferenceImage(referenceImage *Image, referenceID int32, config *SubjectReferenceConfig) *SubjectReferenceImage
- func NewSubjectReferenceImage(referenceImage *Image, referenceID int32, config *SubjectReferenceConfig) *SubjectReferenceImage
- type SubjectReferenceType
- type SupervisedHyperParameters
- type SupervisedTuningDataStats
- func (s *SupervisedTuningDataStats) MarshalJSON() ([]byte, error) func (s *SupervisedTuningDataStats) UnmarshalJSON(data []byte) error
- func (s *SupervisedTuningDataStats) MarshalJSON() ([]byte, error)
- func (s *SupervisedTuningDataStats) UnmarshalJSON(data []byte) error
- type SupervisedTuningDatasetDistribution
- type SupervisedTuningDatasetDistributionDatasetBucket
- type SupervisedTuningSpec
- type ThinkingConfig
- type ThinkingLevel
- type Tokens
- func (m Tokens) Create(ctx context.Context, config *CreateAuthTokenConfig) (*AuthToken, error)
- func (m Tokens) Create(ctx context.Context, config *CreateAuthTokenConfig) (*AuthToken, error)
- type TokensInfo
- func (t *TokensInfo) MarshalJSON() ([]byte, error) func (t *TokensInfo) UnmarshalJSON(data []byte) error
- func (t *TokensInfo) MarshalJSON() ([]byte, error)
- func (t *TokensInfo) UnmarshalJSON(data []byte) error
- type Tool
- type ToolCodeExecution
- type ToolConfig
- type TrafficType
- type Transcription
- type TunedModel
- type TunedModelCheckpoint
- type TunedModelInfo
- func (t *TunedModelInfo) MarshalJSON() ([]byte, error) func (t *TunedModelInfo) UnmarshalJSON(data []byte) error
- func (t *TunedModelInfo) MarshalJSON() ([]byte, error)
- func (t *TunedModelInfo) UnmarshalJSON(data []byte) error
- type TuningDataStats
- type TuningDataset
- type TuningExample
- type TuningJob
- func (t *TuningJob) MarshalJSON() ([]byte, error) func (t *TuningJob) UnmarshalJSON(data []byte) error
- func (t *TuningJob) MarshalJSON() ([]byte, error)
- func (t *TuningJob) UnmarshalJSON(data []byte) error
- type TuningMethod
- type TuningMode
- type TuningOperation
- type TuningTask
- type TuningValidationDataset
- type Tunings
- func (m Tunings) All(ctx context.Context) iter.Seq2[*TuningJob, error] func (m Tunings) Cancel(ctx context.Context, name string, config *CancelTuningJobConfig) (*CancelTuningJobResponse, error) func (t Tunings) Get(ctx context.Context, name string, config *GetTuningJobConfig) (*TuningJob, error) func (m Tunings) List(ctx context.Context, config *ListTuningJobsConfig) (Page[TuningJob], error) func (t Tunings) Tune(ctx context.Context, baseModel string, trainingDataset *TuningDataset, ...) (*TuningJob, error)
- func (m Tunings) All(ctx context.Context) iter.Seq2[*TuningJob, error]
- func (m Tunings) Cancel(ctx context.Context, name string, config *CancelTuningJobConfig) (*CancelTuningJobResponse, error)
- func (t Tunings) Get(ctx context.Context, name string, config *GetTuningJobConfig) (*TuningJob, error)
- func (m Tunings) List(ctx context.Context, config *ListTuningJobsConfig) (Page[TuningJob], error)
- func (t Tunings) Tune(ctx context.Context, baseModel string, trainingDataset *TuningDataset, ...) (*TuningJob, error)
- type TurnCompleteReason
- type TurnCoverage
- type Type
- type URLContext
- type URLContextMetadata
- type URLMetadata
- type URLRetrievalStatus
- type UpdateCachedContentConfig
- func (u *UpdateCachedContentConfig) MarshalJSON() ([]byte, error) func (u *UpdateCachedContentConfig) UnmarshalJSON(data []byte) error
- func (u *UpdateCachedContentConfig) MarshalJSON() ([]byte, error)
- func (u *UpdateCachedContentConfig) UnmarshalJSON(data []byte) error
- type UpdateModelConfig
- type UploadFileConfig
- type UploadToFileSearchStoreConfig
- type UploadToFileSearchStoreOperation
- type UploadToFileSearchStoreResponse
- type UploadToFileSearchStoreResumableResponse
- type UpscaleImageConfig
- type UpscaleImageResponse
- type UrlRetrievalStatus
- type UsageMetadata
- type VADSignalType
- type VeoHyperParameters
- type VeoTuningSpec
- type VertexAISearch
- type VertexAISearchDataStoreSpec
- type VertexRAGStore
- type VertexRAGStoreRAGResource
- type Video
- type VideoCompressionQuality
- type VideoGenerationMask
- type VideoGenerationMaskMode
- type VideoGenerationReferenceImage
- type VideoGenerationReferenceType
- type VideoMetadata
- func (c *VideoMetadata) MarshalJSON() ([]byte, error) func (c *VideoMetadata) UnmarshalJSON(data []byte) error
- func (c *VideoMetadata) MarshalJSON() ([]byte, error)
- func (c *VideoMetadata) UnmarshalJSON(data []byte) error
- type VoiceActivity
- type VoiceActivityDetectionSignal
- type VoiceActivityType
- type VoiceConfig
- type WhiteSpaceConfig

### Examples ¶

- Chats (Geminiapi)
[LINK: Chats (Geminiapi)](#example-Chats-Geminiapi)
- Chats (Stream_geminiapi)
[LINK: Chats (Stream_geminiapi)](#example-Chats-Stream_geminiapi)
- Chats (Stream_vertexai)
- Chats (Vertexai)
- Models.GenerateContent (CodeExecution_geminiapi)
[LINK: Models.GenerateContent (CodeExecution_geminiapi)](#example-Models.GenerateContent-CodeExecution_geminiapi)
- Models.GenerateContent (CodeExecution_vertexai)
- Models.GenerateContent (Config_geminiapi)
[LINK: Models.GenerateContent (Config_geminiapi)](#example-Models.GenerateContent-Config_geminiapi)
- Models.GenerateContent (Config_vertexai)
- Models.GenerateContent (GcsURI_vertexai)
- Models.GenerateContent (GoogleSearchRetrieval_geminiapi)
[LINK: Models.GenerateContent (GoogleSearchRetrieval_geminiapi)](#example-Models.GenerateContent-GoogleSearchRetrieval_geminiapi)
- Models.GenerateContent (GoogleSearchRetrieval_vertexai)
- Models.GenerateContent (HttpURL_vertexai)
- Models.GenerateContent (InlineAudio_geminiapi)
[LINK: Models.GenerateContent (InlineAudio_geminiapi)](#example-Models.GenerateContent-InlineAudio_geminiapi)
- Models.GenerateContent (InlineAudio_vertexai)
- Models.GenerateContent (InlineImage_geminiapi)
[LINK: Models.GenerateContent (InlineImage_geminiapi)](#example-Models.GenerateContent-InlineImage_geminiapi)
- Models.GenerateContent (InlineImage_vertexai)
- Models.GenerateContent (InlinePDF_geminiapi)
[LINK: Models.GenerateContent (InlinePDF_geminiapi)](#example-Models.GenerateContent-InlinePDF_geminiapi)
- Models.GenerateContent (InlinePDF_vertexai)
- Models.GenerateContent (InlineVideo_geminiapi)
[LINK: Models.GenerateContent (InlineVideo_geminiapi)](#example-Models.GenerateContent-InlineVideo_geminiapi)
- Models.GenerateContent (InlineVideo_vertexai)
- Models.GenerateContent (SystemInstruction_geminiapi)
[LINK: Models.GenerateContent (SystemInstruction_geminiapi)](#example-Models.GenerateContent-SystemInstruction_geminiapi)
- Models.GenerateContent (SystemInstruction_vertexai)
- Models.GenerateContent (Text_geminiapi)
[LINK: Models.GenerateContent (Text_geminiapi)](#example-Models.GenerateContent-Text_geminiapi)
- Models.GenerateContent (Text_vertexai)
- Models.GenerateContent (Texts_geminiapi)
[LINK: Models.GenerateContent (Texts_geminiapi)](#example-Models.GenerateContent-Texts_geminiapi)
- Models.GenerateContent (Texts_vertexai)
- Models.GenerateContent (ThirdPartyModel_vertexai)
- Models.GenerateContentStream (Text_geminiapi)
[LINK: Models.GenerateContentStream (Text_geminiapi)](#example-Models.GenerateContentStream-Text_geminiapi)
- Models.GenerateContentStream (Text_vertexai)
- NewClient (Geminiapi)
[LINK: NewClient (Geminiapi)](#example-NewClient-Geminiapi)
- NewClient (Vertexai)

### Constants ¶

[LINK: View Source](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1243)

### Variables ¶

[LINK: View Source](https://github.com/googleapis/go-genai/blob/v1.44.0/pages.go#L24)
ErrPageDone is the error returned by an iterator's Next method when no more pages are available.

### Functions ¶

[LINK: ConvertBidiSetupToTokenSetup](https://github.com/googleapis/go-genai/blob/v1.44.0/tokens.go#L84)
Convert BidiGenerateContentSetup to token setup.
[LINK: Ptr](https://github.com/googleapis/go-genai/blob/v1.44.0/common.go#L36)
Ptr returns a pointer to its argument.
It can be used to initialize pointer fields:
[LINK: SetDefaultBaseURLs](https://github.com/googleapis/go-genai/blob/v1.44.0/base_url.go#L33)
SetDefaultBaseURLs overrides the base URLs for the Gemini API and Vertex AI API.
[HTTPOptions.BaseURL] takes precedence over URLs set here.
Note: This function should be called before initializing the SDK. If the
base URLs are set after initializing the SDK, the base URLs will not be
updated.

### Types ¶

[LINK: APIAuth](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1479)
[LINK: APIAuthAPIKeyConfig](#APIAuthAPIKeyConfig)
The generic reusable API auth config. Deprecated. Please use AuthConfig (google/cloud/aiplatform/master/auth.proto)
instead. This data type is not supported in Gemini API.
[LINK: APIAuthAPIKeyConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1470)
The API secret. This data type is not supported in Gemini API.
[LINK: APIError](https://github.com/googleapis/go-genai/blob/v1.44.0/api_client.go#L466)
APIError contains an error response from the server.
[LINK: Error](https://github.com/googleapis/go-genai/blob/v1.44.0/api_client.go#L506)
[LINK: APIError](#APIError)
Error returns a string representation of the APIError.
[LINK: APIKeyConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1486)
[LINK: https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents](https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents)
[LINK: https://example.com/act?api_key=](https://example.com/act?api_key=)
Config for authentication with API key. This data type is not supported in Gemini
API.
[LINK: APISpec](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L95)
The API spec that the external API implements. This enum is not supported in Gemini
API.
[LINK: APISpec](#APISpec)
[LINK: APISpec](#APISpec)
[LINK: APISpec](#APISpec)
[LINK: ActivityEnd](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6288)
Marks the end of user activity.
This can only be sent if automatic (i.e. server-side) activity detection is
disabled.
[LINK: ActivityHandling](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L833)
The different ways of handling user activity.
[LINK: ActivityStart](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6282)
Marks the start of user activity.
This can only be sent if automatic (i.e. server-side) activity detection is
disabled.
[LINK: AdapterSize](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L463)
Adapter size for tuning. This enum is not supported in Gemini API.
[LINK: AudioTranscriptionConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6211)
The audio transcription configuration in Setup.
[LINK: AuthConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1552)
[LINK: APIKeyConfig](#APIKeyConfig)
Auth configuration to run the extension. This data type is not supported in Gemini
API.
[LINK: AuthConfigGoogleServiceAccountConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1505)
[LINK: https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents](https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents)
Config for Google Service Account Authentication. This data type is not supported
in Gemini API.
[LINK: AuthConfigHTTPBasicAuthConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1515)
[LINK: https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents](https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents)
Config for HTTP Basic Authentication. This data type is not supported in Gemini API.
[LINK: AuthConfigOauthConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1525)
[LINK: https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents](https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents)
Config for user oauth. This data type is not supported in Gemini API.
[LINK: AuthConfigOidcConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1537)
[LINK: https://cloud.google.com/iam/docs/create-short-lived-credentials-direct#sa-credentials-oidc](https://cloud.google.com/iam/docs/create-short-lived-credentials-direct#sa-credentials-oidc)
[LINK: https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents](https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents)
Config for user OIDC auth. This data type is not supported in Gemini API.
[LINK: AuthToken](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6464)
Config for auth_tokens.create parameters.
[LINK: AuthType](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L107)
Type of auth scheme. This enum is not supported in Gemini API.
[LINK: AutomaticActivityDetection](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6144)
Configures automatic detection of activity.
[LINK: Backend](https://github.com/googleapis/go-genai/blob/v1.44.0/client.go#L56)
Backend is the GenAI backend to use for the client.
[LINK: String](https://github.com/googleapis/go-genai/blob/v1.44.0/client.go#L72)
The Stringer interface for Backend.
[LINK: BaseURLParameters](https://github.com/googleapis/go-genai/blob/v1.44.0/base_url.go#L21)
BaseURLParameters are parameters for setting the base URLs for the Gemini API and Vertex AI API.
[LINK: BatchJob](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5453)
Config for batches.create return value.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5517)
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5482)
[LINK: BatchJobDestination](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5399)
Config for `des` parameter.
[LINK: BatchJobSource](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5345)
Config for `src` parameter.
[LINK: Batches](https://github.com/googleapis/go-genai/blob/v1.44.0/batches.go#L894)
Batches provides methods for managing the batch jobs.
You don't need to initiate this struct. Create a client instance via NewClient, and
then access Batches through client.Batches field.
[LINK: All](https://github.com/googleapis/go-genai/blob/v1.44.0/batches.go#L1369)
All retrieves all batch_jobs resources.
This method handles pagination internally, making multiple API calls as needed
to fetch all entries. It returns an iterator that yields each "batchJobs"
entry one by one. You do not need to manage pagination
tokens or make multiple calls to retrieve all data.
[LINK: Cancel](https://github.com/googleapis/go-genai/blob/v1.44.0/batches.go#L1144)
Cancel cancels a batch job resource.
[LINK: Create](https://github.com/googleapis/go-genai/blob/v1.44.0/batches.go#L1389)
Create a batch job.
[LINK: CreateEmbeddings](https://github.com/googleapis/go-genai/blob/v1.44.0/batches.go#L1417)
Create an embeddings batch job.
[LINK: Delete](https://github.com/googleapis/go-genai/blob/v1.44.0/batches.go#L1274)
Delete deletes a batch job resource.
[LINK: Get](https://github.com/googleapis/go-genai/blob/v1.44.0/batches.go#L1062)
Get gets a batch job resource.
[LINK: List](https://github.com/googleapis/go-genai/blob/v1.44.0/batches.go#L1346)
List retrieves a paginated list of batch_jobs resources.
[LINK: Behavior](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L165)
Specifies the function Behavior. Currently only supported by the BidiGenerateContent
method. This enum is not supported in Vertex AI.
[LINK: Blob](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1030)
Content blob.
[LINK: BlockedReason](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L386)
The reason why the prompt was blocked.
[LINK: CachedContent](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4634)
A resource used in LLM queries for users to explicitly specify what to cache.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4681)
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4651)
[LINK: CachedContentUsageMetadata](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4620)
Metadata on the usage of the cached content.
[LINK: Caches](https://github.com/googleapis/go-genai/blob/v1.44.0/caches.go#L482)
Caches provides methods for managing the context caching.
You don't need to initiate this struct. Create a client instance via NewClient, and
then access Caches through client.Caches field.
[LINK: All](https://github.com/googleapis/go-genai/blob/v1.44.0/caches.go#L878)
All retrieves all cached_contents resources.
This method handles pagination internally, making multiple API calls as needed
to fetch all entries. It returns an iterator that yields each "cachedContents"
entry one by one. You do not need to manage pagination
tokens or make multiple calls to retrieve all data.
[LINK: Create](https://github.com/googleapis/go-genai/blob/v1.44.0/caches.go#L487)
Create creates a new cached content resource.
[LINK: Delete](https://github.com/googleapis/go-genai/blob/v1.44.0/caches.go#L637)
Delete deletes a cached content resource.
[LINK: Get](https://github.com/googleapis/go-genai/blob/v1.44.0/caches.go#L562)
Get gets a cached content resource.
[LINK: List](https://github.com/googleapis/go-genai/blob/v1.44.0/caches.go#L855)
List retrieves a paginated list of cached_contents resources.
[LINK: Update](https://github.com/googleapis/go-genai/blob/v1.44.0/caches.go#L709)
Update updates a cached content resource.
[LINK: CancelBatchJobConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5579)
Optional parameters.
[LINK: CancelTuningJobConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4427)
Optional parameters for tunings.cancel method.
[LINK: CancelTuningJobResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4433)
Empty response for tunings.cancel method.
[LINK: Candidate](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2577)
A response candidate generated from the model.
[LINK: Chat](https://github.com/googleapis/go-genai/blob/v1.44.0/chats.go#L38)
Chat represents a single chat session (multi-turn conversation) with the model.
[LINK: History](https://github.com/googleapis/go-genai/blob/v1.44.0/chats.go#L166)
History returns the chat history. Returns the curated history if
curated is true, otherwise returns the comprehensive history.
[LINK: Send](https://github.com/googleapis/go-genai/blob/v1.44.0/chats.go#L184)
Send function sends the conversation history with the additional user's message and returns the model's response.
[LINK: SendMessage](https://github.com/googleapis/go-genai/blob/v1.44.0/chats.go#L174)
SendMessage is a wrapper around Send.
[LINK: SendMessageStream](https://github.com/googleapis/go-genai/blob/v1.44.0/chats.go#L207)
SendMessageStream is a wrapper around SendStream.
[LINK: SendStream](https://github.com/googleapis/go-genai/blob/v1.44.0/chats.go#L217)
SendStream function sends the conversation history with the additional user's message and returns the model's response.
[LINK: Chats](https://github.com/googleapis/go-genai/blob/v1.44.0/chats.go#L29)
Chats provides util functions for creating a new chat session.
You don't need to initiate this struct. Create a client instance via NewClient, and
then access Chats through client.Models field.
[LINK: Create](https://github.com/googleapis/go-genai/blob/v1.44.0/chats.go#L126)
Create initializes a new chat session.
[LINK: Checkpoint](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3413)
Describes the machine learning model version checkpoint.
[LINK: ChunkingConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5057)
Config for telling the service how to chunk the file.
[LINK: Citation](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2266)
Source attributions for content. This data type is not supported in Gemini API.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2301)
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2281)
[LINK: CitationMetadata](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2318)
Citation information when the model quotes another source.
[LINK: Client](https://github.com/googleapis/go-genai/blob/v1.44.0/client.go#L31)
Client is the GenAI client. It provides access to the various GenAI services.
[LINK: NewClient](https://github.com/googleapis/go-genai/blob/v1.44.0/client.go#L188)
NewClient creates a new GenAI client.
You can configure the client by passing in a ClientConfig struct.
If a nil ClientConfig is provided, the client will be configured using
default settings and environment variables:
- Environment Variables for BackendGeminiAPI:
Environment Variables for BackendGeminiAPI:
- GEMINI_API_KEY: Specifies the API key for the Gemini API.
GEMINI_API_KEY: Specifies the API key for the Gemini API.
- GOOGLE_API_KEY: Can also be used to specify the API key for the Gemini API.
If both GOOGLE_API_KEY and GEMINI_API_KEY are set, GOOGLE_API_KEY will be used.
GOOGLE_API_KEY: Can also be used to specify the API key for the Gemini API.
If both GOOGLE_API_KEY and GEMINI_API_KEY are set, GOOGLE_API_KEY will be used.
- Environment Variables for BackendVertexAI:
Environment Variables for BackendVertexAI:
- GOOGLE_GENAI_USE_VERTEXAI: Must be set to "1" or "true" to use the Vertex AI
backend.
GOOGLE_GENAI_USE_VERTEXAI: Must be set to "1" or "true" to use the Vertex AI
backend.
- GOOGLE_CLOUD_PROJECT: Required. Specifies the GCP project ID.
GOOGLE_CLOUD_PROJECT: Required. Specifies the GCP project ID.
- GOOGLE_CLOUD_LOCATION or GOOGLE_CLOUD_REGION: Required. Specifies the GCP
location/region.
GOOGLE_CLOUD_LOCATION or GOOGLE_CLOUD_REGION: Required. Specifies the GCP
location/region.
If using the Vertex AI backend and no credentials are provided in the
ClientConfig, the client will attempt to use application default credentials.
This example shows how to create a new client for Gemini API.
This example shows how to create a new client for Vertex AI.
[LINK: ClientConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/client.go#L350)
ClientConfig returns the ClientConfig for the client.
The returned ClientConfig is a copy of the ClientConfig used to create the client.
[LINK: ClientConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/client.go#L84)
[LINK: https://ai.google.dev/gemini-api/docs/api-key](https://ai.google.dev/gemini-api/docs/api-key)
[LINK: https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
[LINK: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations)
[LINK: https://developers.google.com/accounts/docs/application-default-credentials](https://developers.google.com/accounts/docs/application-default-credentials)
ClientConfig is the configuration for the GenAI client.
[LINK: UseDefaultCredentials](https://github.com/googleapis/go-genai/blob/v1.44.0/client.go#L360)
UseDefaultCredentials sets the credentials to use default credentials and
add authorization middleware to the HTTP client.
If the ClientConfig already has credentials, this method will return an error.
Use this method if your provided HTTPClient doesn't handles credentials.
[LINK: CodeExecutionResult](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L870)
Result of executing the ExecutableCode . Only generated when using the [CodeExecution]
tool, and always follows a `part` containing the ExecutableCode .
[LINK: CompletionStats](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5436)
Success and error statistics of processing multiple entities (for example, DataItems
or structured data rows) in batch. This data type is not supported in Gemini API.
[LINK: ComputeTokensConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3617)
Optional parameters for computing tokens.
[LINK: ComputeTokensResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3669)
Response for computing tokens.
[LINK: ComputeTokensResult](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6557)
Local tokenizer compute tokens result.
[LINK: ComputerUse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1446)
Tool to support computer use.
[LINK: Content](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1232)
Contains the multi-part content of a message.
[LINK: NewContentFromBytes](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1277)
NewContentFromBytes builds a Content from a byte slice and mime type.
If role is the empty string, it defaults to RoleUser .
[LINK: NewContentFromCodeExecutionResult](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1332)
NewContentFromCodeExecutionResult builds a Content from a given Outcome and std output of the code execution.
If role is the empty string, it defaults to RoleUser .
[LINK: NewContentFromExecutableCode](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1321)
NewContentFromExecutableCode builds a Content from a single piece of source code in the given Language .
If role is the empty string, it defaults to RoleUser .
[LINK: NewContentFromFunctionCall](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1299)
NewContentFromFunctionCall builds a Content from a single FunctionCall given the function name and args.
If role is the empty string, it defaults to RoleUser .
[LINK: NewContentFromFunctionResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1310)
NewContentFromFunctionResponse builds a Content from a single FunctionResponse given the function name and response.
If role is the empty string, it defaults to RoleUser .
[LINK: NewContentFromParts](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1257)
NewContentFromParts builds a Content from a list of parts and a Role .
If role is the empty string, it defaults to RoleUser .
[LINK: NewContentFromText](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1266)
NewContentFromText builds a Content from a text string.
If role is the empty string, it defaults to RoleUser .
[LINK: NewContentFromURI](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1288)
NewContentFromURI builds a Content from a file URI and mime type.
If role is the empty string, it defaults to RoleUser .
[LINK: Text](https://github.com/googleapis/go-genai/blob/v1.44.0/models_helpers.go#L18)
Text returns a slice of Content with a single Part with the given text.
[LINK: ContentEmbedding](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2864)
The embedding generated from an input content.
[LINK: ContentEmbeddingStatistics](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2855)
Statistics of the input text associated with the result of content embedding.
[LINK: ContentReferenceImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5918)
A content reference image.
A content reference image represents a subject to reference (ex. person,
product, animal) provided by the user. It can optionally be provided in
addition to a style reference image (ex. background, style reference).
[LINK: NewContentReferenceImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3113)
NewContentReferenceImage creates a new ContentReferenceImage.
[LINK: ContextWindowCompressionConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6202)
Enables context window compression -- mechanism managing model context window so
it does not exceed given length.
[LINK: ControlReferenceConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3003)
Configuration for a Control reference image.
[LINK: ControlReferenceImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5844)
A control image is an image that represents a sketch image of areas for the model
to fill in based on the prompt. Its image is either a control image provided by the
user, or a regular image which the backend will use to generate a control image of.
In the case of the latter, the EnableControlImageComputation field in the config
should be set to true.
[LINK: NewControlReferenceImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3083)
NewControlReferenceImage creates a new ControlReferenceImage.
[LINK: ControlReferenceType](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L620)
Enum representing the control type of a control reference image.
[LINK: CountTokensConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3592)
Config for the count_tokens method.
[LINK: CountTokensResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3606)
Response for counting tokens.
[LINK: CountTokensResult](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6551)
Local tokenizer count tokens result.
[LINK: CreateAuthTokenConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6480)
Optional parameters.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6529)
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6504)
[LINK: CreateBatchJobConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5424)
Config for optional parameters.
[LINK: CreateCachedContentConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4545)
[LINK: https://cloud.google.com/vertex-ai/docs/general/cmek](https://cloud.google.com/vertex-ai/docs/general/cmek)
Optional configuration for cached content creation.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4598)
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4573)
[LINK: CreateEmbeddingsBatchJobConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5565)
Config for optional parameters.
[LINK: CreateFileConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5299)
Used to override the default configuration.
[LINK: CreateFileResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5308)
Response for the create file method.
[LINK: CreateFileSearchStoreConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4933)
Optional parameters for creating a file search store.
[LINK: CreateTuningJobConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4466)
Fine-tuning job creation request - optional fields.
[LINK: CustomMetadata](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4819)
User provided metadata stored as key-value pairs. This data type is not supported
in Vertex AI.
[LINK: DatasetDistribution](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4011)
Distribution computed over a tuning dataset. This data type is not supported in Gemini
API.
[LINK: DatasetDistributionDistributionBucket](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4000)
Dataset bucket used to create a histogram for the distribution given a population
of values. This data type is not supported in Gemini API.
[LINK: DatasetStats](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4032)
Statistics computed over a tuning dataset. This data type is not supported in Gemini
API.
[LINK: DeleteBatchJobConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5611)
Optional parameters for models.get method.
[LINK: DeleteCachedContentConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4714)
Optional parameters for caches.delete method.
[LINK: DeleteCachedContentResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4720)
Empty response for caches.delete method.
[LINK: DeleteDocumentConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4899)
Config for optional parameters.
[LINK: DeleteFileConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5320)
Used to override the default configuration.
[LINK: DeleteFileResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5326)
Response for the delete file method.
[LINK: DeleteFileSearchStoreConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5014)
Optional parameters for deleting a FileSearchStore.
[LINK: DeleteModelConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3516)
Configuration for deleting a tuned model.
[LINK: DeleteModelResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3521)
[LINK: DeleteResourceJob](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5617)
The return value of delete operation.
[LINK: DistillationDataStats](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4053)
Statistics computed for datasets used for distillation. This data type is not supported
in Gemini API.
[LINK: DistillationHyperParameters](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3930)
Hyperparameters for Distillation. This data type is not supported in Gemini API.
[LINK: DistillationSpec](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3941)
[LINK: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/tuning#supported_models](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/tuning#supported_models)
Distillation tuning spec for tuning.
[LINK: Document](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4831)
A Document is a collection of Chunks.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4877)
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4852)
[LINK: DocumentState](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L723)
State for the lifecycle of a Document.
[LINK: Documents](https://github.com/googleapis/go-genai/blob/v1.44.0/documents.go#L124)
[LINK: All](https://github.com/googleapis/go-genai/blob/v1.44.0/documents.go#L368)
All retrieves all documents resources.
This method handles pagination internally, making multiple API calls as needed
to fetch all entries. It returns an iterator that yields each "documents"
entry one by one. You do not need to manage pagination
tokens or make multiple calls to retrieve all data.
[LINK: Delete](https://github.com/googleapis/go-genai/blob/v1.44.0/documents.go#L203)
[LINK: Get](https://github.com/googleapis/go-genai/blob/v1.44.0/documents.go#L128)
[LINK: List](https://github.com/googleapis/go-genai/blob/v1.44.0/documents.go#L345)
List retrieves a paginated list of documents resources.
[LINK: DownloadFileConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5755)
Used to override the default configuration.
[LINK: DownloadURI](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5259)
DownloadURI represents a resource that can be downloaded.
It is used to abstract the different types of resources that can be downloaded,
such as files or videos
You can create instances that implement this interface using the following
constructor functions:
- NewDownloadURIFromFile
- NewDownloadURIFromVideo
- NewDownloadURIFromGeneratedVideo
- ...
[LINK: NewDownloadURIFromFile](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5265)
NewDownloadURIFromFile creates a DownloadURI from a File .
[LINK: NewDownloadURIFromGeneratedVideo](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5275)
NewDownloadURIFromVideo creates a DownloadURI from a GeneratedVideo .
[LINK: NewDownloadURIFromVideo](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5270)
NewDownloadURIFromVideo creates a DownloadURI from a Video .
[LINK: DynamicRetrievalConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1873)
Describes the options to customize dynamic retrieval.
[LINK: DynamicRetrievalConfigMode](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L180)
The mode of the predictor to be used in dynamic retrieval.
[LINK: EditImageConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3122)
Configuration for editing an image.
[LINK: EditImageResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3171)
Response for the request to edit an image.
[LINK: EditMode](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L640)
Enum representing the editing mode.
[LINK: EmbedContentBatch](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5549)
Parameters for the embed_content method.
[LINK: EmbedContentConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2833)
Optional parameters for the EmbedContent method.
[LINK: EmbedContentMetadata](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2873)
Request-level metadata for the Vertex Embed Content API.
[LINK: EmbedContentResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2880)
Response for the embed_content method.
[LINK: EmbeddingsBatchJobSource](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5556)
[LINK: EncryptionSpec](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4211)
Represents a customer-managed encryption key spec that can be applied to a top-level
resource. This data type is not supported in Gemini API.
[LINK: EndSensitivity](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L821)
End of speech sensitivity.
[LINK: Endpoint](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3349)
An endpoint where models are deployed.
[LINK: EnterpriseWebSearch](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1738)
Tool to search public web data, powered by Vertex AI Search and Sec4 compliance.
This data type is not supported in Gemini API.
[LINK: EntityLabel](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3321)
An entity representing the segmented area.
[LINK: Environment](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L555)
The environment being operated.
[LINK: ExecutableCode](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L882)
Code generated by the model that is meant to be executed, and the result returned
to the model. Generated when using the [CodeExecution] tool, in which the code will
be automatically executed, and a corresponding CodeExecutionResult will also be
generated.
[LINK: ExternalAPI](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1587)
[LINK: APIAuth](#APIAuth)
[LINK: APISpec](#APISpec)
[LINK: ExternalAPIElasticSearchParams](#ExternalAPIElasticSearchParams)
[LINK: ExternalAPISimpleSearchParams](#ExternalAPISimpleSearchParams)
Retrieve from data source powered by external API for grounding. The external API
is not owned by Google, but need to follow the pre-defined API spec. This data type
is not supported in Gemini API.
[LINK: ExternalAPIElasticSearchParams](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1569)
The search parameters to use for the ELASTIC_SEARCH spec. This data type is not supported
in Gemini API.
[LINK: ExternalAPISimpleSearchParams](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1581)
The search parameters to use for SIMPLE_SEARCH spec. This data type is not supported
in Gemini API.
[LINK: ExtrasRequestProvider](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1370)
ExtrasRequestProvider provides a way to dynamically modify the request body
before it is sent. It is a function that takes the request body and returns
the modified body. This is useful for advanced scenarios where request
parameters need to be added based on logic that cannot
be handled by a static map.
[LINK: FeatureSelectionPreference](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L545)
Options for feature selection preference.
[LINK: FetchPredictOperationConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5633)
[LINK: File](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5154)
A file uploaded to the API.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5222)
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5192)
[LINK: FileData](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L890)
URI based data.
[LINK: FileSearch](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1458)
Tool to retrieve knowledge from the File Search Stores.
[LINK: FileSearchStore](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4941)
A collection of Documents.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4986)
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4961)
[LINK: FileSearchStores](https://github.com/googleapis/go-genai/blob/v1.44.0/filesearchstores.go#L302)
[LINK: All](https://github.com/googleapis/go-genai/blob/v1.44.0/filesearchstores.go#L776)
All retrieves all file_search_stores resources.
This method handles pagination internally, making multiple API calls as needed
to fetch all entries. It returns an iterator that yields each "fileSearchStores"
entry one by one. You do not need to manage pagination
tokens or make multiple calls to retrieve all data.
[LINK: Create](https://github.com/googleapis/go-genai/blob/v1.44.0/filesearchstores.go#L307)
[LINK: Delete](https://github.com/googleapis/go-genai/blob/v1.44.0/filesearchstores.go#L457)
[LINK: Get](https://github.com/googleapis/go-genai/blob/v1.44.0/filesearchstores.go#L382)
[LINK: ImportFile](https://github.com/googleapis/go-genai/blob/v1.44.0/filesearchstores.go#L670)
[LINK: List](https://github.com/googleapis/go-genai/blob/v1.44.0/filesearchstores.go#L753)
List retrieves a paginated list of file_search_stores resources.
[LINK: UploadToFileSearchStore](https://github.com/googleapis/go-genai/blob/v1.44.0/filesearchstores.go#L796)
Upload copies the contents of the given io.Reader to a file search store and return the long running operation.
[LINK: UploadToFileSearchStoreFromPath](https://github.com/googleapis/go-genai/blob/v1.44.0/filesearchstores.go#L839)
UploadToFileSearchStoreFromPath uploads a file from the specified path to a file search store and return the long running operation.
[LINK: FileSource](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L743)
Source of the File.
[LINK: FileState](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L733)
State for the lifecycle of a File.
[LINK: FileStatus](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5142)
Status of a File that uses a common error model.
[LINK: Files](https://github.com/googleapis/go-genai/blob/v1.44.0/files.go#L148)
[LINK: All](https://github.com/googleapis/go-genai/blob/v1.44.0/files.go#L457)
All retrieves all files resources.
This method handles pagination internally, making multiple API calls as needed
to fetch all entries. It returns an iterator that yields each "files"
entry one by one. You do not need to manage pagination
tokens or make multiple calls to retrieve all data.
[LINK: Delete](https://github.com/googleapis/go-genai/blob/v1.44.0/files.go#L361)
[LINK: Download](https://github.com/googleapis/go-genai/blob/v1.44.0/files.go#L478)
Download function downloads a file from the specified URI.
If the URI refers to a video( Video , GeneratedVideo ), the video bytes will be populated to the video's VideoBytes field.
[LINK: Get](https://github.com/googleapis/go-genai/blob/v1.44.0/files.go#L296)
[LINK: List](https://github.com/googleapis/go-genai/blob/v1.44.0/files.go#L434)
List retrieves a paginated list of files resources.
[LINK: Upload](https://github.com/googleapis/go-genai/blob/v1.44.0/files.go#L509)
Upload copies the contents of the given io.Reader to file storage associated
with the service, and returns information about the resulting file.
[LINK: UploadFromPath](https://github.com/googleapis/go-genai/blob/v1.44.0/files.go#L559)
UploadFromPath uploads a file from the specified path and returns information
about the resulting file.
[LINK: FinishReason](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L294)
The reason why the model stopped generating tokens.
If empty, the model has not stopped generating the tokens.
[LINK: FunctionCall](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L923)
A function call.
[LINK: FunctionCallingConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1947)
Function calling config.
[LINK: FunctionCallingConfigMode](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L190)
Function calling mode.
[LINK: FunctionDeclaration](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1752)
Structured representation of a function declaration as defined by the [OpenAPI 3.0
specification]( https://spec.openapis.org/oas/v3.0.3 ). Included in this declaration
are the function name, description, parameters and response type. This FunctionDeclaration
is a representation of a block of code that can be used as a `Tool` by the model
and executed by the client.
[LINK: https://spec.openapis.org/oas/v3.0.3](https://spec.openapis.org/oas/v3.0.3)
[LINK: FunctionResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1002)
A function response.
[LINK: FunctionResponseBlob](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L946)
Raw media bytes for function response.
Text should not be sent as raw bytes, use the FunctionResponse.response
field.
[LINK: FunctionResponseFileData](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L957)
URI based data for function response.
[LINK: FunctionResponsePart](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L974)
A datatype containing media that is part of a `FunctionResponse` message.
A `FunctionResponsePart` consists of data which has an associated datatype. A
`FunctionResponsePart` can only contain one of the accepted types in
`FunctionResponsePart.data`.
A `FunctionResponsePart` must have a fixed IANA MIME type identifying the
type and subtype of the media if the `inline_data` field is filled with raw
bytes.
[LINK: NewFunctionResponsePartFromBytes](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L992)
NewFunctionResponsePartFromBytes builds a FunctionResponsePart from a given byte array and mime type.
[LINK: NewFunctionResponsePartFromURI](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L982)
NewFunctionResponsePartFromURI builds a FunctionResponsePart from a given file URI and mime type.
[LINK: FunctionResponseScheduling](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L56)
Specifies how the response should be scheduled in the conversation.
[LINK: GeminiPreferenceExample](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4068)
Input example for preference optimization. This data type is not supported in Gemini
API.
[LINK: GeminiPreferenceExampleCompletion](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4059)
Completion and its preference score. This data type is not supported in Gemini API.
[LINK: GenerateContentConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2095)
[LINK: https://spec.openapis.org/oas/v3.0.3#schema](https://spec.openapis.org/oas/v3.0.3#schema)
Optional model configuration parameters.
For more information, see `Content generation parameters
< https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters >`_.
[LINK: https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters)
[LINK: ToGenerationConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2216)
[LINK: GenerateContentResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2663)
Response message for PredictionService.GenerateContent.
[LINK: CodeExecutionResult](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2814)
CodeExecutionResult returns the code execution result in the GenerateContentResponse.
[LINK: ExecutableCode](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2795)
ExecutableCode returns the executable code in the GenerateContentResponse.
[LINK: FunctionCalls](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2771)
FunctionCalls returns the list of function calls in the GenerateContentResponse.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2703)
[LINK: Text](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2720)
Text concatenates all the text parts in the GenerateContentResponse.
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2683)
[LINK: GenerateContentResponsePromptFeedback](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2608)
Content filter results for a prompt sent in the request. Note: This is sent only
in the first stream chunk and only if no candidates were generated due to content
violations.
[LINK: GenerateContentResponseUsageMetadata](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2629)
Usage metadata about the content generation request and response. This message provides
a detailed breakdown of token usage and other relevant metrics. This data type is
not supported in Gemini API.
[LINK: GenerateImagesConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2893)
The configuration for generating images. You can find API default values and more
details at VertexAI: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api .
GeminiAPI: https://ai.google.dev/gemini-api/docs/imagen#imagen-model
[LINK: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api)
[LINK: https://ai.google.dev/gemini-api/docs/imagen#imagen-model](https://ai.google.dev/gemini-api/docs/imagen#imagen-model)
[LINK: GenerateImagesResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2979)
The output images response.
[LINK: GenerateVideosConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3730)
You can find API default values and more details at VertexAI: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation .
[LINK: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation)
[LINK: GenerateVideosOperation](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3806)
A video generation operation.
[LINK: GenerateVideosResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3796)
Response with generated videos.
[LINK: GenerateVideosSource](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3698)
A set of source input(s) for video generation.
[LINK: GeneratedImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2964)
An output image.
[LINK: GeneratedImageMask](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3329)
A generated image mask.
[LINK: GeneratedVideo](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3781)
A generated video.
[LINK: GenerationConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3528)
[LINK: https://spec.openapis.org/oas/v3.0.3#schema](https://spec.openapis.org/oas/v3.0.3#schema)
Generation config. You can find API default values and more details at https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig and https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters .
[LINK: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#generationconfig)
[LINK: https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters)
[LINK: GenerationConfigRoutingConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2064)
The configuration for routing the request to a specific model. This data type is
not supported in Gemini API.
[LINK: GenerationConfigRoutingConfigAutoRoutingMode](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2050)
When automated routing is specified, the routing will be determined by the pretrained
routing model and customer provided model routing preference. This data type is not
supported in Gemini API.
[LINK: GenerationConfigRoutingConfigManualRoutingMode](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2057)
[LINK: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#supported-models](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#supported-models)
When manual routing is set, the specified model will be used directly. This data
type is not supported in Gemini API.
[LINK: GenerationConfigThinkingConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1377)
Config for thinking feature.
This struct will be deprecated. Please use ThinkingConfig instead.
[LINK: GetBatchJobConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5573)
Optional parameters.
[LINK: GetCachedContentConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4708)
Optional parameters for caches.get method.
[LINK: GetDocumentConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4805)
Optional Config.
[LINK: GetFileConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5314)
Used to override the default configuration.
[LINK: GetFileSearchStoreConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5008)
Optional parameters for getting a FileSearchStore.
[LINK: GetModelConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3343)
Optional parameters for models.get method.
[LINK: GetOperationConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5628)
[LINK: GetTuningJobConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3826)
Optional parameters for tunings.get method.
[LINK: GoogleMaps](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1790)
Tool to retrieve public maps data for grounding, powered by Google.
[LINK: GoogleRpcStatus](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3971)
The `Status` type defines a logical error model that is suitable for different programming
environments, including REST APIs and RPC APIs. It is used by [gRPC]( https://github.com/grpc ).
Each `Status` message contains three pieces of data: error code, error message, and
error details. You can find out more about this error model and how to work with
it in the [API Design Guide]( https://cloud.google.com/apis/design/errors ). This data
type is not supported in Gemini API.
[LINK: https://github.com/grpc](https://github.com/grpc)
[LINK: https://cloud.google.com/apis/design/errors](https://cloud.google.com/apis/design/errors)
[LINK: GoogleSearch](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1858)
GoogleSearch tool type. Tool to support Google Search in Model. Powered by Google.
[LINK: GoogleSearchRetrieval](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1882)
Tool to retrieve public web data for grounding, powered by Google.
[LINK: GroundingChunk](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2426)
Grounding chunk.
[LINK: GroundingChunkMaps](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2366)
Chunk from Google Maps. This data type is not supported in Gemini API.
[LINK: GroundingChunkMapsPlaceAnswerSources](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2358)
Sources used to generate the place answer. This data type is not supported in Gemini
API.
[LINK: GroundingChunkMapsPlaceAnswerSourcesAuthorAttribution](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2327)
Author attribution for a photo or review. This data type is not supported in Gemini
API.
[LINK: GroundingChunkMapsPlaceAnswerSourcesReviewSnippet](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2337)
Encapsulates a review snippet. This data type is not supported in Gemini API.
[LINK: GroundingChunkRetrievedContext](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2401)
Chunk from context retrieved by the retrieval tools. This data type is not supported
in Gemini API.
[LINK: GroundingChunkWeb](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2416)
Chunk from the web.
[LINK: GroundingMetadata](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2492)
Metadata returned to client when grounding is enabled.
[LINK: GroundingMetadataSourceFlaggingURI](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2484)
Source content flagging URI for a place or review. This is currently populated only
for Google Maps grounding. This data type is not supported in Gemini API.
[LINK: GroundingSupport](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2451)
Grounding support.
[LINK: HTTPElementLocation](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L126)
The location of the API key. This enum is not supported in Gemini API.
[LINK: HTTPOptions](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1342)
[LINK: https://generativelanguage.googleapis.com/](https://generativelanguage.googleapis.com/)
[LINK: https://us-central1-aiplatform.googleapis.com/](https://us-central1-aiplatform.googleapis.com/)
[LINK: https://cloud.google.com/vertex-ai/docs/reference/rest](https://cloud.google.com/vertex-ai/docs/reference/rest)
[LINK: https://ai.google.dev/api/rest](https://ai.google.dev/api/rest)
HTTP options to be used in each of the requests.
[LINK: HTTPResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2258)
A wrapper class for the HTTP response.
[LINK: HarmBlockMethod](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L263)
Specify if the threshold is used for probability or severity score. If not specified,
the threshold is used for probability score. This enum is not supported in Gemini
API.
[LINK: HarmBlockThreshold](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L275)
The harm block threshold.
[LINK: HarmCategory](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L229)
Harm category.
[LINK: HarmProbability](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L336)
Harm probability levels in the content.
[LINK: HarmSeverity](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L352)
Harm severity levels in the content. This enum is not supported in Gemini API.
[LINK: Image](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2942)
An image.
[LINK: ImageConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2028)
The image generation configuration to be used in GenerateContentConfig.
[LINK: ImagePromptLanguage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L587)
Enum that specifies the language of the text in the prompt.
[LINK: ImportFileConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5087)
Optional parameters for importing a file.
[LINK: ImportFileOperation](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5107)
Long-running operation for importing a file to a FileSearchStore.
[LINK: ImportFileResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5097)
Response for ImportFile to import a File API file with a file search store.
[LINK: InlinedEmbedContentResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5391)
Config for `inlined_embedding_responses` parameter.
[LINK: InlinedRequest](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5332)
[LINK: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models)
Config for inlined request.
[LINK: InlinedResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5373)
Config for `inlined_responses` parameter.
[LINK: Interval](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1802)
Represents a time interval, encoded as a Timestamp start (inclusive) and a Timestamp
end (exclusive). The start must be less than or equal to the end. When the start
equals the end, the interval is empty (matches no time). When both start and end
are unspecified, the interval matches any time.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1836)
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1811)
[LINK: JobError](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5361)
Job error.
[LINK: JobState](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L483)
Job state.
[LINK: Language](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L46)
Programming language of the `code`.
[LINK: LatLng](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1931)
An object that represents a latitude/longitude pair.
This is expressed as a pair of doubles to represent degrees latitude and
degrees longitude. Unless specified otherwise, this object must conform to the
<a href=" https://en.wikipedia.org/wiki/World_Geodetic_System#1984_version ">
WGS84 standard</a>. Values must be within normalized ranges.
[LINK: ListBatchJobsConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5585)
Config for optional parameters.
[LINK: ListBatchJobsResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5601)
Config for batches.list return value.
[LINK: ListCachedContentsConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4782)
Config for caches.list method.
[LINK: ListCachedContentsResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4795)
[LINK: ListDocumentsConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4908)
Config for optional parameters.
[LINK: ListDocumentsResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4922)
Config for documents.list return value.
[LINK: ListFileSearchStoresConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5025)
Optional parameters for listing FileSearchStore.
[LINK: ListFileSearchStoresResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5039)
Config for file_search_stores.list return value.
[LINK: ListFilesConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5128)
Used to override the default configuration.
[LINK: ListFilesResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5289)
Response for the list files method.
[LINK: ListModelsConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3476)
[LINK: ListModelsResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3494)
[LINK: ListTuningJobsConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4400)
Configuration for the list tuning jobs method.
[LINK: ListTuningJobsResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4416)
Response for the list tuning jobs method.
[LINK: Live](https://github.com/googleapis/go-genai/blob/v1.44.0/live.go#L39)
Preview. Live serves as the entry point for establishing real-time WebSocket
connections to the API. It manages the initial handshake and setup process.
It is initiated when creating a client via NewClient . You don't need to
create a new Live object directly. Access it through the `Live` field of a
`Client` instance.
[LINK: Connect](https://github.com/googleapis/go-genai/blob/v1.44.0/live.go#L54)
Preview. Connect establishes a WebSocket connection to the specified
model with the given configuration. It sends the initial
setup message and returns a Session object representing the connection.
[LINK: LiveClientContent](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6267)
Incremental update of the current conversation delivered from the client.
All the content here will unconditionally be appended to the conversation
history and used as part of the prompt to the model to generate content.
A message here will interrupt any current model generation.
[LINK: LiveClientContentInput](https://github.com/googleapis/go-genai/blob/v1.44.0/live.go#L154)
Preview. LiveClientContentInput is the input for [SendClientContent].
[LINK: LiveClientMessage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6348)
Messages sent by the client in the API call.
[LINK: LiveClientRealtimeInput](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6303)
User input that is sent in real time.
This is different from `LiveClientContent` in a few ways:
- Can be sent continuously without interruption to model generation.
- If there is a need to mix data interleaved across the
`LiveClientContent` and the `LiveClientRealtimeInput`, server attempts to
optimize for best response, but there are no guarantees.
- End of turn is not explicitly specified, but is rather derived from user
activity (for example, end of speech).
- Even before the end of turn, the data is processed incrementally
to optimize for a fast start of the response from the model.
- Is always assumed to be the user's input (cannot be used to populate
conversation history).
[LINK: LiveClientSetup](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6224)
Message contains configuration that will apply for the duration of the streaming
session.
[LINK: LiveClientToolResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6319)
Client generated response to a `ToolCall` received from the server.
Individual `FunctionResponse` objects are matched to the respective
`FunctionCall` objects by the `id` field.
Note that in the unary and server-streaming GenerateContent APIs function
calling happens by exchanging the `Content` parts, while in the bidi
GenerateContent APIs function calling happens over this dedicated set of
messages.
[LINK: LiveConnectConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6361)
Session config for the API connection.
[LINK: LiveConnectConstraints](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6470)
[LINK: https://ai.google.dev/gemini-api/docs/models](https://ai.google.dev/gemini-api/docs/models)
Config for LiveConnectConstraints for Auth Token creation.
[LINK: LiveRealtimeInput](https://github.com/googleapis/go-genai/blob/v1.44.0/live.go#L195)
Preview. LiveRealtimeInput is the input for [SendRealtimeInput].
[LINK: LiveSendClientContentParameters](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6432)
Parameters for sending client content to the live API.
[LINK: LiveSendRealtimeInputParameters](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6325)
Parameters for sending realtime input to the live API.
[LINK: LiveSendToolResponseParameters](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6452)
Parameters for sending tool responses to the live API.
[LINK: LiveServerContent](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5952)
Incremental server update generated by the model in response to client messages.
Content is generated as quickly as possible, and not in real time. Clients
may choose to buffer and play it out in real time.
[LINK: LiveServerGoAway](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6041)
Server will not be able to service client soon.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6068)
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6048)
[LINK: LiveServerMessage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6120)
Response message for API call.
[LINK: LiveServerSessionResumptionUpdate](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6086)
Update of the session resumption state.
Only sent if `session_resumption` was set in the connection config.
[LINK: LiveServerSetupComplete](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5936)
Sent in response to a `LiveGenerateContentSetup` message from the client.
[LINK: LiveServerToolCall](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5995)
Request for the client to execute the `function_calls` and return the responses with
the matching `id`s.
[LINK: LiveServerToolCallCancellation](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6005)
Notification for the client that a previously issued `ToolCallMessage` with the specified
`id`s should have been not executed and should be cancelled.
If there were side-effects to those tool calls, clients may attempt to undo
the tool calls. This message occurs only in cases where the clients interrupt
server turns.
[LINK: LiveToolResponseInput](https://github.com/googleapis/go-genai/blob/v1.44.0/live.go#L235)
Preview. LiveToolResponseInput is the input for [SendToolResponse].
[LINK: LogprobsResult](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2532)
Logprobs Result
[LINK: LogprobsResultCandidate](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2516)
Candidate for the logprobs token and score.
[LINK: LogprobsResultTopCandidates](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2526)
Candidates with top log probabilities at each decoding step.
[LINK: MaskReferenceConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2990)
Configuration for a Mask reference image.
[LINK: MaskReferenceImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5819)
A mask reference image. This encapsulates either a mask image provided by the user
and configs for the user provided mask, or only config parameters for the model to
generate a mask. A mask image is an image whose non-zero values indicate where to
edit the base image. If the user provides a mask image, the mask must be in the same
dimensions as the raw image.
[LINK: NewMaskReferenceImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3073)
NewMaskReferenceImage creates a new MaskReferenceImage.
[LINK: MaskReferenceMode](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L609)
Enum representing the mask mode of a mask reference image.
[LINK: MediaModality](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L767)
Server content modalities.
[LINK: MediaResolution](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L437)
The media resolution to use.
[LINK: Modality](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L423)
Server content modalities.
[LINK: ModalityTokenCount](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2619)
Represents token counting info for a single modality.
[LINK: Model](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3423)
A trained machine learning model.
[LINK: ModelArmorConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2085)
Configuration for Model Armor integrations of prompt and responses. This data type
is not supported in Gemini API.
[LINK: ModelSelectionConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1440)
Config for model selection.
[LINK: Models](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L4043)
Models provides methods for interacting with the available language models.
You don't need to initiate this struct. Create a client instance via NewClient, and
then access Models through client.Models field.
[LINK: All](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L5238)
All retrieves all models resources.
This method handles pagination internally, making multiple API calls as needed
to fetch all entries. It returns an iterator that yields each cached
content entry one by one. You do not need to manage pagination
tokens or make multiple calls to retrieve all data.
[LINK: ComputeTokens](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L5035)
ComputeTokens computes the number of tokens for the provided contents.
[LINK: CountTokens](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L4963)
CountTokens counts the number of tokens in the provided contents.
[LINK: Delete](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L4891)
Delete deletes a specific model resource by its name.
[LINK: EditImage](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L5311)
EditImage edits an image based on the provided model, prompt, reference images, and configuration.
[LINK: EmbedContent](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L4183)
EmbedContent generates embeddings for the provided contents using the specified model.
[LINK: GenerateContent](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L5190)
GenerateContent generates content based on the provided model, contents, and configuration.
This example shows how to call the GenerateContent method with code execution to Gemini API.
This example shows how to call the GenerateContent method with code execution to Vertex AI.
This example shows how to call the GenerateContent method with GenerateContentConfig to Gemini API.
This example shows how to call the GenerateContent method with GenerateContentConfig to Vertex AI.
This example shows how to call the GenerateContent method with GCS URI to Vertex AI.
This example shows how to call the GenerateContent method with Google Search Retrieval to Gemini API.
This example shows how to call the GenerateContent method with Google Search Retrieval to Vertex AI.
This example shows how to call the GenerateContent method with HTTP URL to Vertex AI.
This example shows how to call the GenerateContent method with a inline audio file to Gemini API.
This example shows how to call the GenerateContent method with a inline audio file to Vertex AI.
This example shows how to call the GenerateContent method with inline image to Gemini API.
This example shows how to call the GenerateContent method with inline image to Vertex AI.
This example shows how to call the GenerateContent method with a inline pdf file to Gemini API.
This example shows how to call the GenerateContent method with a inline pdf file to Vertex AI.
This example shows how to call the GenerateContent method with a inline video file to Gemini API.
This example shows how to call the GenerateContent method with a inline video file to Vertex AI.
This example shows how to call the GenerateContent method with system instruction to Gemini API.
This example shows how to call the GenerateContent method with system instruction to Vertex AI.
This example shows how to call the GenerateContent method with a simple text to Gemini API.
This example shows how to call the GenerateContent method with a simple text to Vertex AI.
This example shows how to call the GenerateContent method with multiple texts to Gemini API.
This example shows how to call the GenerateContent method with multiple texts to Vertex AI.
This example shows how to call the GenerateContent method with third party model to Vertex AI.
[LINK: GenerateContentStream](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L5198)
GenerateContentStream generates a stream of content based on the provided model, contents, and configuration.
This example shows how to call the GenerateContentStream method with a simple text to Gemini API.
This example shows how to call the GenerateContentStream method with a simple text to Vertex AI.
[LINK: GenerateImages](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L5262)
GenerateImages generates images based on the provided model, prompt, and configuration.
[LINK: GenerateVideos](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L5321)
GenerateVideos creates a long-running video generation operation.
This method is kept for backward compatibility. Use GenerateVideosFromSource instead.
[LINK: GenerateVideosFromSource](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L5327)
GenerateVideos creates a long-running video generation operation.
[LINK: Get](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L4643)
Get retrieves a specific model resource by its name.
[LINK: List](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L5206)
List retrieves a paginated list of models resources.
[LINK: RecontextImage](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L4477)
RecontextImage recontextualizes an image.
There are two types of recontextualization currently supported:
1) Imagen Product Recontext - Generate images of products in new scenes
and contexts.
2) Virtual Try-On: Generate images of persons modeling fashion products.
[LINK: SegmentImage](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L4560)
SegmentImage segments an image, creating a mask of a specified area.
[LINK: Update](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L4809)
Update updates a specific model resource.
[LINK: UpscaleImage](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go#L5291)
UpscaleImage upscales an image using the specified model, image, upscale factor, and configuration.
[LINK: MultiSpeakerVoiceConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2000)
Configuration for a multi-speaker text-to-speech request.
[LINK: Operations](https://github.com/googleapis/go-genai/blob/v1.44.0/operations.go#L125)
Operations provides methods for managing the long-running operations.
You don't need to initiate this struct. Create a client instance via NewClient, and
then access Operations through client.Operations field.
[LINK: GetImportFileOperation](https://github.com/googleapis/go-genai/blob/v1.44.0/operations.go#L504)
GetImportFileOperation retrieves the status and result of a long-running import file to file search store operation.
If the operation is still in progress, the returned ImportFileOperation
will have Done set to false. If the operation has completed successfully,
Done will be true, and the Result field will contain the result. If the
operation failed, Done will be true, and the Error field will be populated.
[LINK: GetUploadToFileSearchStoreOperation](https://github.com/googleapis/go-genai/blob/v1.44.0/operations.go#L487)
GetUploadToFileSearchStoreOperation retrieves the status and result of a long-running upload to file search store operation.
If the operation is still in progress, the returned UploadToFileSearchStoreOperation
will have Done set to false. If the operation has completed successfully,
Done will be true, and the Result field will contain the result. If the
operation failed, Done will be true, and the Error field will be populated.
[LINK: GetVideosOperation](https://github.com/googleapis/go-genai/blob/v1.44.0/operations.go#L460)
GetVideosOperation retrieves the status and result of a long-running video generation operation.
If the operation is still in progress, the returned GenerateVideosOperation
will have Done set to false. If the operation has completed successfully,
Done will be true, and the Result field will contain the result. If the
operation failed, Done will be true, and the Error field will be populated.
[LINK: Outcome](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L31)
Outcome of the code execution.
[LINK: Page](https://github.com/googleapis/go-genai/blob/v1.44.0/pages.go#L28)
Page represents a page of results from a paginated API call.
It contains a slice of items and information about the next page.
[LINK: Next](https://github.com/googleapis/go-genai/blob/v1.44.0/pages.go#L86)
Next retrieves the next page of results.
If there are no more pages, PageDone is returned.  Otherwise,
a new Page struct containing the next set of results is returned.
Any other errors encountered during retrieval will also be returned.
[LINK: Part](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1114)
A datatype containing media content.
Exactly one field within a Part should be set, representing the specific type
of content being conveyed. Using multiple fields within the same `Part`
instance is considered invalid.
[LINK: NewPartFromBytes](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1171)
NewPartFromBytes builds a Part from a given byte array and mime type.
[LINK: NewPartFromCodeExecutionResult](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1222)
NewPartFromCodeExecutionResult builds a CodeExecutionResult Part from the given Outcome and std output.
[LINK: NewPartFromExecutableCode](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1212)
NewPartFromExecutableCode builds a ExecutableCode Part from a single piece of source code in the given Language .
[LINK: NewPartFromFile](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1154)
NewPartFromFile builds a Part from a given File .
[LINK: NewPartFromFunctionCall](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1181)
NewPartFromFunctionCall builds a FunctionCall Part from the given function name and args.
[LINK: NewPartFromFunctionResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1191)
NewPartFromFunctionResponse builds a FunctionResponse Part from the given function name and response.
[LINK: NewPartFromFunctionResponseWithParts](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1201)
NewPartFromFunctionResponseWithParts builds a FunctionResponse Part from the given function name, response and function response parts.
[LINK: NewPartFromText](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1164)
NewPartFromText builds a Part from a given text.
[LINK: NewPartFromURI](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1144)
NewPartFromURI builds a Part from a given file URI and mime type.
[LINK: PartMediaResolution](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L861)
Media resolution for the input media.
[LINK: PartMediaResolutionLevel](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L529)
The tokenization quality used for given media.
[LINK: PartialArg](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L905)
Partial argument value of the function call. This data type is not supported in Gemini
API.
[LINK: PartnerModelTuningSpec](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4219)
Tuning spec for Partner models. This data type is not supported in Gemini API.
[LINK: PersonGeneration](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L575)
Enum that controls the generation of people.
[LINK: PhishBlockThreshold](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L144)
Sites with confidence level chosen & above this value will be blocked from the search
results. This enum is not supported in Gemini API.
[LINK: PreTunedModel](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3985)
A pre-tuned model for continuous tuning. This data type is not supported in Gemini
API.
[LINK: PrebuiltVoiceConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1978)
The configuration for the prebuilt speaker to use.
[LINK: PreferenceOptimizationDataStats](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4077)
Statistics computed for datasets used for preference optimization. This data type
is not supported in Gemini API.
[LINK: PreferenceOptimizationHyperParameters](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3901)
Hyperparameters for Preference Optimization. This data type is not supported in Gemini
API.
[LINK: PreferenceOptimizationSpec](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3914)
Preference optimization tuning spec for tuning.
[LINK: ProactivityConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6215)
Config for proactivity features.
[LINK: ProductImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3223)
An image of the product.
[LINK: RAGChunk](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2392)
A RAGChunk includes the content of a chunk of a RAGFile, and associated metadata.
This data type is not supported in Gemini API.
[LINK: RAGChunkPageSpan](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2383)
Represents where the chunk starts and ends in the document. This data type is not
supported in Gemini API.
[LINK: RAGRetrievalConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1683)
Specifies the context retrieval config. This data type is not supported in Gemini
API.
[LINK: RAGRetrievalConfigFilter](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1643)
Config for filters. This data type is not supported in Gemini API.
[LINK: RAGRetrievalConfigHybridSearch](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1653)
Config for Hybrid Search. This data type is not supported in Gemini API.
[LINK: RAGRetrievalConfigRanking](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1674)
Config for ranking and reranking. This data type is not supported in Gemini API.
[LINK: RAGRetrievalConfigRankingLlmRanker](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1662)
[LINK: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#supported-models](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#supported-models)
Config for LlmRanker. This data type is not supported in Gemini API.
[LINK: RAGRetrievalConfigRankingRankService](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1668)
Config for Rank Service. This data type is not supported in Gemini API.
[LINK: RawReferenceImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5797)
A raw reference image.
A raw reference image represents the base image to edit, provided by the user.
It can optionally be provided in addition to a mask reference image or
a style reference image.
[LINK: NewRawReferenceImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3064)
NewRawReferenceImage creates a new RawReferenceImage.
[LINK: RealtimeInputConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6166)
Marks the end of user activity.
This can only be sent if automatic (i.e. server-side) activity detection is
disabled.
[LINK: RecontextImageConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3241)
Configuration for recontextualizing an image.
[LINK: RecontextImageResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3272)
The output images response.
[LINK: RecontextImageSource](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3229)
A set of source input(s) for image recontextualization.
[LINK: ReferenceImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3059)
ReferenceImage is an interface that represents a generic reference image.
You can create instances that implement this interface using the following
constructor functions:
- NewRawReferenceImage
- NewMaskReferenceImage
- NewControlReferenceImage
- NewStyleReferenceImage
- NewSubjectReferenceImage
- NewContentReferenceImage
- ...
[LINK: ReplicatedVoiceConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1970)
ReplicatedVoiceConfig is used to configure replicated voice.
[LINK: Retrieval](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1718)
[LINK: ExternalAPI](#ExternalAPI)
Defines a retrieval tool that model can call to access external knowledge. This data
type is not supported in Gemini API.
[LINK: RetrievalConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1939)
Retrieval config.
[LINK: RetrievalMetadata](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2465)
Metadata related to retrieval in the grounding flow.
[LINK: Role](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1241)
[LINK: SafetyAttributes](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2954)
Safety attributes of a GeneratedImage or the user-provided prompt.
[LINK: SafetyFilterLevel](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L565)
Enum that controls the safety filter level for objectionable content.
[LINK: SafetyRating](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2541)
Safety rating corresponding to the generated content.
[LINK: SafetySetting](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2072)
Safety settings.
[LINK: Schema](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1386)
Schema is used to define the format of input/output data.
Represents a select subset of an [OpenAPI 3.0 schema
object]( https://spec.openapis.org/oas/v3.0.3#schema-object ). More fields may
be added in the future as needed.
You can find more details and examples at https://spec.openapis.org/oas/v3.0.3.html#schema-object
[LINK: https://spec.openapis.org/oas/v3.0.3#schema-object](https://spec.openapis.org/oas/v3.0.3#schema-object)
[LINK: https://spec.openapis.org/oas/v3.0.3.html#schema-object](https://spec.openapis.org/oas/v3.0.3.html#schema-object)
[LINK: ScribbleImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3278)
An image mask representing a brush scribble.
[LINK: SearchEntryPoint](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2475)
Google search entry point.
[LINK: Segment](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2437)
Segment of the content.
[LINK: SegmentImageConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3296)
Configuration for segmenting an image.
[LINK: SegmentImageResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3337)
The output images response.
[LINK: SegmentImageSource](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3284)
A set of source input(s) for image segmentation.
[LINK: SegmentMode](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L654)
Enum that represents the segmentation mode.
[LINK: Session](https://github.com/googleapis/go-genai/blob/v1.44.0/live.go#L46)
Preview. Session represents an active, real-time WebSocket connection to the
Generative AI API. It provides methods for sending client messages and
receiving server messages over the established connection.
[LINK: Close](https://github.com/googleapis/go-genai/blob/v1.44.0/live.go#L318)
Preview. Close terminates the connection.
[LINK: Receive](https://github.com/googleapis/go-genai/blob/v1.44.0/live.go#L284)
Preview. Receive reads a LiveServerMessage from the connection.
This method blocks until a message is received from the server.
The returned message represents a part of or a complete model turn.
If the received message is a LiveServerToolCall , the user must call
[SendToolResponse] to provide the function execution result and continue the turn.
[LINK: SendClientContent](https://github.com/googleapis/go-genai/blob/v1.44.0/live.go#L190)
Preview. SendClientContent transmits non-realtime, turn-based content to the model
over the established WebSocket connection.
There are two primary ways to send messages in a live session:
[SendClientContent] and [SendRealtimeInput].
Messages sent via [SendClientContent] are added to the model's context strictly
**in the order they are sent**. A conversation using [SendClientContent] is
similar to using the Chat.SendMessageStream method, but the conversation
history state is managed by the API server.
Due to this ordering guarantee, the model might not respond as quickly to
[SendClientContent] messages compared to SendRealtimeInput messages. This latency
difference is most noticeable when sending content that requires significant
preprocessing, such as images.
[SendClientContent] accepts a LiveClientContentInput which contains a list of *Content objects, offering more flexibility than the *Blob used by
SendRealtimeInput.
Key use cases for [SendClientContent] over SendRealtimeInput include:
- Pre-populating the conversation context (including sending content types
not supported by realtime messages) before starting a realtime interaction.
- Conducting a non-realtime conversation, similar to client.Chats.SendMessage,
using the live API infrastructure.
Caution: Interleaving [SendClientContent] and SendRealtimeInput within the
same conversation is not recommended and may lead to unexpected behavior.
The input parameter of type LiveClientContentInput contains:
- Turns: A slice of *Content objects representing the message(s) to send.
- TurnComplete: If true (the default), the model will reply immediately.
If false, the model waits for subsequent SendClientContent calls until
one is sent with TurnComplete set to true.
[LINK: SendRealtimeInput](https://github.com/googleapis/go-genai/blob/v1.44.0/live.go#L209)
Preview. SendRealtimeInput transmits realtime audio chunks and video frames (images)
to the model over the established WebSocket connection.
Use SendRealtimeInput for streaming audio and video data. The API automatically
responds to audio based on voice activity detection (VAD).
SendRealtimeInput is optimized for responsiveness, potentially at the expense
of deterministic ordering. Audio and video tokens are added to the model's
context as they become available, allowing for faster interaction.
It accepts a LiveRealtimeInput parameter containing the media data.
Only one argument (e.g., Media, Audio, Video, Text) should be provided per call.
[LINK: SendToolResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/live.go#L243)
Preview. SendToolResponse transmits a LiveClientToolResponse over the established WebSocket connection.
Use SendToolResponse to reply to LiveServerToolCall messages received from the server.
To define the available tools for the session, set the [LiveConnectConfig.Tools]
field when establishing the connection via Live.Connect .
[LINK: SessionResumptionConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6179)
Configuration of session resumption mechanism.
Included in `LiveConnectConfig.session_resumption`. If included server
will send `LiveServerSessionResumptionUpdate` messages.
[LINK: SingleEmbedContentResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5383)
Config for `response` parameter.
[LINK: SlidingWindow](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6193)
Context window will be truncated by keeping only suffix of it.
Context window will always be cut at start of USER role turn. System
instructions and `BidiGenerateContentSetup.prefix_turns` will not be
subject to the sliding window mechanism, they will always stay at the
beginning of context window.
[LINK: SpeakerVoiceConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1991)
Configuration for a single speaker in a multi speaker setup.
[LINK: SpeechConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2006)
[LINK: StartSensitivity](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L809)
Start of speech sensitivity.
[LINK: StringList](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4812)
User provided string values assigned to a single metadata key. This data type is
not supported in Vertex AI.
[LINK: StyleReferenceConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3013)
Configuration for a Style reference image.
[LINK: StyleReferenceImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5869)
A style reference image.
This encapsulates a style reference image provided by the user, and
additionally optional config parameters for the style reference image.
A raw reference image can also be provided as a destination for the style to
be applied to.
[LINK: NewStyleReferenceImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3093)
NewStyleReferenceImage creates a new ControlReferenceImage.
[LINK: SubjectReferenceConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3019)
Configuration for a Subject reference image.
[LINK: SubjectReferenceImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5894)
A subject reference image.
This encapsulates a subject reference image provided by the user, and
additionally optional config parameters for the subject reference image.
A raw reference image can also be provided as a destination for the subject to
be applied to.
[LINK: NewSubjectReferenceImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3103)
NewSubjectReferenceImage creates a new SubjectReferenceImage.
[LINK: SubjectReferenceType](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L630)
Enum representing the subject type of a subject reference image.
[LINK: SupervisedHyperParameters](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3863)
Hyperparameters for SFT. This data type is not supported in Gemini API.
[LINK: SupervisedTuningDataStats](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4132)
Tuning data statistics for Supervised Tuning. This data type is not supported in
Gemini API.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4182)
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4162)
[LINK: SupervisedTuningDatasetDistribution](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4109)
Dataset distribution for Supervised Tuning. This data type is not supported in Gemini
API.
[LINK: SupervisedTuningDatasetDistributionDatasetBucket](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4098)
Dataset bucket used to create a histogram for the distribution given a population
of values. This data type is not supported in Gemini API.
[LINK: SupervisedTuningSpec](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3880)
Supervised tuning spec for tuning.
[LINK: ThinkingConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2017)
The thinking features configuration.
[LINK: ThinkingLevel](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L213)
The number of thoughts tokens that the model should generate.
[LINK: Tokens](https://github.com/googleapis/go-genai/blob/v1.44.0/tokens.go#L186)
Tokens provides methods for managing the context caching.
You don't need to initiate this struct. Create a client instance via NewClient, and
then access Tokens through client.Tokens field.
[LINK: Create](https://github.com/googleapis/go-genai/blob/v1.44.0/tokens.go#L191)
Create creates a new cached content resource.
[LINK: TokensInfo](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3623)
Tokens info with a list of tokens and the corresponding list of token ids.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3652)
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3632)
[LINK: Tool](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1892)
Tool details of a tool that the model may use to generate a response.
[LINK: ToolCodeExecution](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1733)
Tool that executes code generated by the model, and automatically returns the result
to the model. See also [ExecutableCode]and CodeExecutionResult which are input
and output to this tool. This data type is not supported in Gemini API.
[LINK: ToolConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1962)
Tool config.
This config is shared for all tools provided in the request.
[LINK: TrafficType](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L411)
The traffic type for this request. This enum is not supported in Gemini API.
[LINK: Transcription](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5942)
Audio transcription in Server Conent.
[LINK: TunedModel](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3845)
TunedModel for the Tuned Model of a Tuning Job.
[LINK: TunedModelCheckpoint](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3832)
TunedModelCheckpoint for the Tuned Model of a Tuning Job.
[LINK: TunedModelInfo](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3357)
A tuned machine learning model.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3391)
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3366)
[LINK: TuningDataStats](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4200)
The tuning data statistic values for TuningJob. This data type is not supported in
Gemini API.
[LINK: TuningDataset](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4447)
Supervised fine-tuning training dataset.
[LINK: TuningExample](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4439)
A single example for tuning. This data type is not supported in Vertex AI.
[LINK: TuningJob](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4257)
[LINK: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/tuning#supported_models](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/tuning#supported_models)
[LINK: https://cloud.google.com/iam/docs/service-agents#vertex-ai-secure-fine-tuning-service-agent](https://cloud.google.com/iam/docs/service-agents#vertex-ai-secure-fine-tuning-service-agent)
A tuning job.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4368)
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4333)
[LINK: TuningMethod](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L711)
Enum representing the tuning method.
[LINK: TuningMode](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L451)
Tuning mode. This enum is not supported in Gemini API.
[LINK: TuningOperation](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4525)
A long-running operation.
[LINK: TuningTask](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L515)
The tuning task. Either I2V or T2V. This enum is not supported in Gemini API.
[LINK: TuningValidationDataset](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4457)
[LINK: Tunings](https://github.com/googleapis/go-genai/blob/v1.44.0/tunings.go#L908)
[LINK: All](https://github.com/googleapis/go-genai/blob/v1.44.0/tunings.go#L1294)
All retrieves all tuning_jobs resources.
This method handles pagination internally, making multiple API calls as needed
to fetch all entries. It returns an iterator that yields each "tuningJobs"
entry one by one. You do not need to manage pagination
tokens or make multiple calls to retrieve all data.
[LINK: Cancel](https://github.com/googleapis/go-genai/blob/v1.44.0/tunings.go#L1055)
Cancel cancels a tuning job resource.
[LINK: Get](https://github.com/googleapis/go-genai/blob/v1.44.0/tunings.go#L1361)
Get retrieves a tuning job resource.
[LINK: List](https://github.com/googleapis/go-genai/blob/v1.44.0/tunings.go#L1271)
List retrieves a paginated list of tuning_jobs resources.
[LINK: Tune](https://github.com/googleapis/go-genai/blob/v1.44.0/tunings.go#L1316)
Tune creates a tuning job resource.
[LINK: TurnCompleteReason](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L753)
The reason why the turn is complete.
[LINK: TurnCoverage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L847)
Options about which input is included in the user's turn.
[LINK: Type](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L72)
The type of the data.
[LINK: URLContext](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1888)
Tool to support URL context.
[LINK: URLContextMetadata](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2571)
Metadata related to URL context retrieval tool.
[LINK: URLMetadata](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L2563)
Context of the a single URL retrieval.
[LINK: URLRetrievalStatus](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L368)
Status of the URL retrieval.
[LINK: UpdateCachedContentConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4726)
Optional parameters for caches.update method.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4760)
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4735)
[LINK: UpdateModelConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3504)
Configuration for updating a tuned model.
[LINK: UploadFileConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5741)
Used to override the default configuration.
[LINK: UploadToFileSearchStoreConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5063)
Optional parameters for uploading a file to a FileSearchStore.
[LINK: UploadToFileSearchStoreOperation](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5650)
Long-running operation for uploading a file to a FileSearchStore.
[LINK: UploadToFileSearchStoreResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5640)
The response when long-running operation for uploading a file to a FileSearchStore
complete.
[LINK: UploadToFileSearchStoreResumableResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5081)
Response for the resumable upload method.
[LINK: UpscaleImageConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5764)
Configuration for upscaling an image.
For more information on this configuration, refer to
the `Imagen API reference documentation
< https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api >`_.
[LINK: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api)
[LINK: UpscaleImageResponse](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3215)
[LINK: UrlRetrievalStatus](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1372)
[LINK: UsageMetadata](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6011)
Usage metadata about response(s).
[LINK: VADSignalType](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L785)
The type of the VAD signal.
[LINK: VeoHyperParameters](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4232)
Hyperparameters for Veo. This data type is not supported in Gemini API.
[LINK: VeoTuningSpec](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L4243)
Tuning Spec for Veo Model Tuning. This data type is not supported in Gemini API.
[LINK: VertexAISearch](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1617)
Retrieve from Vertex AI Search datastore or engine for grounding. datastore and engine
are mutually exclusive. See https://cloud.google.com/products/agent-builder . This
data type is not supported in Gemini API.
[LINK: VertexAISearchDataStoreSpec](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1606)
[LINK: https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata](https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata)
Define data stores within engine to filter on in a search call and configurations
for those data stores. For more information, see https://cloud.google.com/generative-ai-app-builder/docs/reference/rpc/google.cloud.discoveryengine.v1#datastorespec .
This data type is not supported in Gemini API.
[LINK: https://cloud.google.com/generative-ai-app-builder/docs/reference/rpc/google.cloud.discoveryengine.v1#datastorespec](https://cloud.google.com/generative-ai-app-builder/docs/reference/rpc/google.cloud.discoveryengine.v1#datastorespec)
[LINK: VertexRAGStore](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1696)
Retrieve from Vertex RAG Store for grounding. This data type is not supported in
Gemini API. You can find API default values and more details at https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/rag-api-v1#parameters-list
[LINK: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/rag-api-v1#parameters-list](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/rag-api-v1#parameters-list)
[LINK: VertexRAGStoreRAGResource](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1634)
The definition of the RAG resource. This data type is not supported in Gemini API.
[LINK: Video](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3679)
A generated video.
[LINK: VideoCompressionQuality](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L699)
Enum that controls the compression quality of the generated videos.
[LINK: VideoGenerationMask](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3720)
A mask for video generation.
[LINK: VideoGenerationMaskMode](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L678)
Enum for the mask mode of a video generation mask.
[LINK: VideoGenerationReferenceImage](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L3711)
A reference image for video generation.
[LINK: VideoGenerationReferenceType](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L665)
Enum for the reference type of a video generation reference image.
[LINK: VideoMetadata](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1044)
Metadata describes the input video content.
[LINK: MarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1087)
[LINK: UnmarshalJSON](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1054)
[LINK: VoiceActivity](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6114)
Voice activity signal.
[LINK: VoiceActivityDetectionSignal](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L6108)
[LINK: VoiceActivityType](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L797)
The type of the voice activity signal.
[LINK: VoiceConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L1983)
[LINK: WhiteSpaceConfig](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go#L5049)
Configuration for a white space chunking algorithm.

## Source Files ¶

[LINK: View all Source files](https://github.com/googleapis/go-genai/tree/v1.44.0)
- api_client.go
[LINK: api_client.go](https://github.com/googleapis/go-genai/blob/v1.44.0/api_client.go)
- base_url.go
[LINK: base_url.go](https://github.com/googleapis/go-genai/blob/v1.44.0/base_url.go)
- batches.go
[LINK: batches.go](https://github.com/googleapis/go-genai/blob/v1.44.0/batches.go)
- caches.go
[LINK: caches.go](https://github.com/googleapis/go-genai/blob/v1.44.0/caches.go)
- chats.go
[LINK: chats.go](https://github.com/googleapis/go-genai/blob/v1.44.0/chats.go)
- client.go
[LINK: client.go](https://github.com/googleapis/go-genai/blob/v1.44.0/client.go)
- common.go
[LINK: common.go](https://github.com/googleapis/go-genai/blob/v1.44.0/common.go)
- documents.go
[LINK: documents.go](https://github.com/googleapis/go-genai/blob/v1.44.0/documents.go)
- files.go
[LINK: files.go](https://github.com/googleapis/go-genai/blob/v1.44.0/files.go)
- filesearchstores.go
[LINK: filesearchstores.go](https://github.com/googleapis/go-genai/blob/v1.44.0/filesearchstores.go)
- live.go
[LINK: live.go](https://github.com/googleapis/go-genai/blob/v1.44.0/live.go)
- live_converters.go
[LINK: live_converters.go](https://github.com/googleapis/go-genai/blob/v1.44.0/live_converters.go)
- models.go
[LINK: models.go](https://github.com/googleapis/go-genai/blob/v1.44.0/models.go)
- models_helpers.go
[LINK: models_helpers.go](https://github.com/googleapis/go-genai/blob/v1.44.0/models_helpers.go)
- operations.go
[LINK: operations.go](https://github.com/googleapis/go-genai/blob/v1.44.0/operations.go)
- pages.go
[LINK: pages.go](https://github.com/googleapis/go-genai/blob/v1.44.0/pages.go)
- replay_api_client.go
[LINK: replay_api_client.go](https://github.com/googleapis/go-genai/blob/v1.44.0/replay_api_client.go)
- replay_sanitizer.go
[LINK: replay_sanitizer.go](https://github.com/googleapis/go-genai/blob/v1.44.0/replay_sanitizer.go)
- tokens.go
[LINK: tokens.go](https://github.com/googleapis/go-genai/blob/v1.44.0/tokens.go)
- tokens_converters.go
[LINK: tokens_converters.go](https://github.com/googleapis/go-genai/blob/v1.44.0/tokens_converters.go)
- transformer.go
[LINK: transformer.go](https://github.com/googleapis/go-genai/blob/v1.44.0/transformer.go)
- tunings.go
[LINK: tunings.go](https://github.com/googleapis/go-genai/blob/v1.44.0/tunings.go)
- types.go
[LINK: types.go](https://github.com/googleapis/go-genai/blob/v1.44.0/types.go)
- types_json.go
[LINK: types_json.go](https://github.com/googleapis/go-genai/blob/v1.44.0/types_json.go)
- version.go
[LINK: version.go](https://github.com/googleapis/go-genai/blob/v1.44.0/version.go)

## Directories ¶


--------------------