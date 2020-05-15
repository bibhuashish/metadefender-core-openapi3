# Go API client for openapi

## Developer Guide
This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form. 
## How to Interact with MetaDefender Core using REST
Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below.
> _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process. 
---
## File Analysis Process

  MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary. 
  Below is a brief description of the API integration flow:

  1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)). 
    
    > _**Note**:_ The performance depends on:      
    > - number of nodes (scaling)
    > - number of engines per node
    > - type of file to be scanned
    > - Metadefender Core and nodes' hardware
  

  2. You have 2 ways to retrieve the analysis report: 
    - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))
  
    > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.
    
    - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete. 

  3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin). 
    - The hash can be found in the scan results

  4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete. 
    > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time. 

---
OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works.


## Overview
This API client was generated by the [OpenAPI Generator](https://openapi-generator.tech) project.  By using the [OpenAPI-spec](https://www.openapis.org/) from a remote server, you can easily generate an API client.

- API version: v4.18.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.GoClientCodegen
For more information, please visit [https://github.com/OPSWAT/metadefender-core-openapi3](https://github.com/OPSWAT/metadefender-core-openapi3)

## Installation

Install the following dependencies:

```shell
go get github.com/stretchr/testify/assert
go get golang.org/x/oauth2
go get golang.org/x/net/context
go get github.com/antihax/optional
```

Put the package under your project folder and add the following in import:

```golang
import "./openapi"
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8008*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminApi* | [**AdminImport**](docs/AdminApi.md#adminimport) | **Post** /admin/import | Import configuration
*AdminApi* | [**RoleCreate**](docs/AdminApi.md#rolecreate) | **Post** /admin/role | Create new role
*AdminApi* | [**UserCreate**](docs/AdminApi.md#usercreate) | **Post** /admin/user | Create user
*AnalysisApi* | [**AnalysisRules**](docs/AnalysisApi.md#analysisrules) | **Get** /file/rules | Fetching Available Analysis Rules
*AnalysisApi* | [**FileAnalysisCancel**](docs/AnalysisApi.md#fileanalysiscancel) | **Post** /file/{data_id}/cancel | Cancel File Analysis
*AnalysisApi* | [**FileAnalysisGet**](docs/AnalysisApi.md#fileanalysisget) | **Get** /file/{data_id} | Fetch Analysis Result
*AnalysisApi* | [**FileAnalysisPost**](docs/AnalysisApi.md#fileanalysispost) | **Post** /file | Analyze File
*AnalysisApi* | [**SanitizedFile**](docs/AnalysisApi.md#sanitizedfile) | **Get** /file/converted/{data_id} | Download Sanitized Files
*AnalysisApi* | [**WebhookStatus**](docs/AnalysisApi.md#webhookstatus) | **Get** /file/webhook/{data_id} | Query webhook status
*AuthApi* | [**UserChangePass**](docs/AuthApi.md#userchangepass) | **Post** /user/changepassword | Change Password
*AuthApi* | [**UserLogin**](docs/AuthApi.md#userlogin) | **Post** /login | Login
*AuthApi* | [**UserLogout**](docs/AuthApi.md#userlogout) | **Post** /logout | Logout
*BatchApi* | [**BatchCancel**](docs/BatchApi.md#batchcancel) | **Post** /file/{batchId}/cancel | Cancel Batch
*BatchApi* | [**BatchClose**](docs/BatchApi.md#batchclose) | **Post** /file/batch/{batchId}/close | Close Batch
*BatchApi* | [**BatchCreate**](docs/BatchApi.md#batchcreate) | **Post** /file/batch | Initiate Batch
*BatchApi* | [**BatchSignedResult**](docs/BatchApi.md#batchsignedresult) | **Get** /file/batch/{batchId}/certificate | Download Signed Batch Result
*BatchApi* | [**BatchStatus**](docs/BatchApi.md#batchstatus) | **Get** /file/batch/{batchId} | Status of Batch Analysis
*ConfigApi* | [**ConfigAuditLog**](docs/ConfigApi.md#configauditlog) | **Put** /admin/config/auditlog | Audit clean up
*ConfigApi* | [**ConfigGetSkipHash**](docs/ConfigApi.md#configgetskiphash) | **Get** /admin/config/skip | Get &#39;skip by hash&#39; list
*ConfigApi* | [**ConfigQuarantine**](docs/ConfigApi.md#configquarantine) | **Put** /admin/config/quarantine | Quarantine clean up
*ConfigApi* | [**ConfigSanitizedRepo**](docs/ConfigApi.md#configsanitizedrepo) | **Put** /admin/config/sanitize | Sanitized files clean up
*ConfigApi* | [**ConfigScanHistory**](docs/ConfigApi.md#configscanhistory) | **Put** /admin/config/scanhistory | Processing history clean up
*ConfigApi* | [**ConfigSession**](docs/ConfigApi.md#configsession) | **Put** /admin/config/session | Session settings
*ConfigApi* | [**ConfigUpdate**](docs/ConfigApi.md#configupdate) | **Put** /admin/config/update | Modules Update Source and Frequency
*ConfigApi* | [**ConfigUpdateSkipHash**](docs/ConfigApi.md#configupdateskiphash) | **Put** /admin/config/skip | Modify &#39;skip by hash&#39; list
*ConfigApi* | [**ConfigUpdateWebhook**](docs/ConfigApi.md#configupdatewebhook) | **Put** /admin/config/webhook | Webhook set configuration
*ConfigApi* | [**ConfigWebhook**](docs/ConfigApi.md#configwebhook) | **Get** /admin/config/webhook | Webhook get configuration
*EnginesApi* | [**EngineDisable**](docs/EnginesApi.md#enginedisable) | **Post** /admin/engine/{engineId}/disable | Disable engines
*EnginesApi* | [**EngineEnable**](docs/EnginesApi.md#engineenable) | **Post** /admin/engine/{engineId}/enable | Enable engines
*EnginesApi* | [**EnginePin**](docs/EnginesApi.md#enginepin) | **Post** /admin/engine/{engineId}/pin | Pin engine to prevent auto-updates
*EnginesApi* | [**EngineUnpin**](docs/EnginesApi.md#engineunpin) | **Post** /admin/engine/{engineId}/unpin | Unpin engine to prevent auto-updates
*LicenseApi* | [**LicenseActivation**](docs/LicenseApi.md#licenseactivation) | **Post** /admin/license/activation | Activate license
*LicenseApi* | [**LicenseGet**](docs/LicenseApi.md#licenseget) | **Get** /admin/license | Get Current License Information
*LicenseApi* | [**LicenseUpload**](docs/LicenseApi.md#licenseupload) | **Post** /admin/license | Upload license key
*StatsApi* | [**EnginesStatus**](docs/StatsApi.md#enginesstatus) | **Get** /stat/engines | Engines Status
*StatsApi* | [**NodesStatus**](docs/StatsApi.md#nodesstatus) | **Get** /stat/nodes | Nodes Status
*StatsApi* | [**ProductVersion**](docs/StatsApi.md#productversion) | **Get** /version | Get Product Version
*YaraApi* | [**YaraPackageGenerate**](docs/YaraApi.md#yarapackagegenerate) | **Put** /yara/generate | Generate Yara package
*YaraApi* | [**YaraPackageStatus**](docs/YaraApi.md#yarapackagestatus) | **Get** /yara/package | Yara Generation Status
*YaraApi* | [**YaraSourcesGet**](docs/YaraApi.md#yarasourcesget) | **Get** /admin/config/yara/sources | Get Yara sources
*YaraApi* | [**YaraSourcesPut**](docs/YaraApi.md#yarasourcesput) | **Put** /admin/config/yara/sources | Modify Yara sources


## Documentation For Models

 - [AdminConfigSession](docs/AdminConfigSession.md)
 - [AdminConfigUpdate](docs/AdminConfigUpdate.md)
 - [AdminConfigUpdateDisabledupdate](docs/AdminConfigUpdateDisabledupdate.md)
 - [AdminConfigWebhook](docs/AdminConfigWebhook.md)
 - [AnalysisResult](docs/AnalysisResult.md)
 - [AnalysisResultProcessInfo](docs/AnalysisResultProcessInfo.md)
 - [AnalysisResultProcessInfoPostProcessing](docs/AnalysisResultProcessInfoPostProcessing.md)
 - [AvEngineScanReport](docs/AvEngineScanReport.md)
 - [BatchId](docs/BatchId.md)
 - [BatchResponse](docs/BatchResponse.md)
 - [BatchResponseBatchFiles](docs/BatchResponseBatchFiles.md)
 - [BatchResponseBatchFilesFilesInBatch](docs/BatchResponseBatchFilesFilesInBatch.md)
 - [BatchResponseBatchFilesProcessInfo](docs/BatchResponseBatchFilesProcessInfo.md)
 - [BatchResponseProcessInfo](docs/BatchResponseProcessInfo.md)
 - [BatchResponseScanResults](docs/BatchResponseScanResults.md)
 - [DeepCdrDetails](docs/DeepCdrDetails.md)
 - [DeepCdrDetailsDetails](docs/DeepCdrDetailsDetails.md)
 - [DlpResponse](docs/DlpResponse.md)
 - [DlpResponseDlpInfo](docs/DlpResponseDlpInfo.md)
 - [DlpResponseDlpInfoHits](docs/DlpResponseDlpInfoHits.md)
 - [DlpResponseDlpInfoHitsCcn](docs/DlpResponseDlpInfoHitsCcn.md)
 - [DlpResponseDlpInfoMetadataRemoval](docs/DlpResponseDlpInfoMetadataRemoval.md)
 - [DlpResponseDlpInfoRedact](docs/DlpResponseDlpInfoRedact.md)
 - [DlpResponseDlpInfoWatermark](docs/DlpResponseDlpInfoWatermark.md)
 - [DlpRuleMatchResult](docs/DlpRuleMatchResult.md)
 - [FileInformation](docs/FileInformation.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2007Issues](docs/InlineResponse2007Issues.md)
 - [InlineResponse2007IssuesGeneral](docs/InlineResponse2007IssuesGeneral.md)
 - [InlineResponse2007IssuesSource](docs/InlineResponse2007IssuesSource.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [InlineResponse403](docs/InlineResponse403.md)
 - [InlineResponse500](docs/InlineResponse500.md)
 - [LicenseInformation](docs/LicenseInformation.md)
 - [MetascanReport](docs/MetascanReport.md)
 - [MetascanReportScanDetails](docs/MetascanReportScanDetails.md)
 - [NewUserRoleRequest](docs/NewUserRoleRequest.md)
 - [NewUserRoleRequestRights](docs/NewUserRoleRequestRights.md)
 - [NewUserRoleResponse](docs/NewUserRoleResponse.md)
 - [NewUserRoleResponseAllOf](docs/NewUserRoleResponseAllOf.md)
 - [ProcessingResultsIndexEnum](docs/ProcessingResultsIndexEnum.md)
 - [ProcessingResultsStringEnum](docs/ProcessingResultsStringEnum.md)
 - [RolePermissionObject](docs/RolePermissionObject.md)
 - [ScanResultEnum](docs/ScanResultEnum.md)
 - [SkipList](docs/SkipList.md)
 - [StatNodesEngines](docs/StatNodesEngines.md)
 - [StatNodesIssues](docs/StatNodesIssues.md)
 - [StatNodesStatuses](docs/StatNodesStatuses.md)
 - [UserLogin](docs/UserLogin.md)
 - [UserRequest](docs/UserRequest.md)
 - [UserRequestAllOf](docs/UserRequestAllOf.md)
 - [UserResponse](docs/UserResponse.md)
 - [VulnerabilityResponse](docs/VulnerabilityResponse.md)
 - [VulnerabilityResponseResult](docs/VulnerabilityResponseResult.md)
 - [VulnerabilityResponseResultDetails](docs/VulnerabilityResponseResultDetails.md)
 - [VulnerabilityResponseResultDetailsCvss](docs/VulnerabilityResponseResultDetailsCvss.md)
 - [VulnerabilityResponseResultDetectedProduct](docs/VulnerabilityResponseResultDetectedProduct.md)
 - [VulnerabilityResponseResultDetectedProductProduct](docs/VulnerabilityResponseResultDetectedProductProduct.md)
 - [VulnerabilityResponseResultDetectedProductVendor](docs/VulnerabilityResponseResultDetectedProductVendor.md)
 - [VulnerabilityResponseResultDetectedProductVersionData](docs/VulnerabilityResponseResultDetectedProductVersionData.md)
 - [VulnerabilityResponseResultVulnerabilites](docs/VulnerabilityResponseResultVulnerabilites.md)
 - [YaraReport](docs/YaraReport.md)
 - [YaraSourcesObject](docs/YaraSourcesObject.md)
 - [YaraSourcesObjectHttpSources](docs/YaraSourcesObjectHttpSources.md)
 - [YaraSourcesObjectLocalSources](docs/YaraSourcesObjectLocalSources.md)


## Documentation For Authorization



## apikey

- **Type**: API key

Example

```golang
auth := context.WithValue(context.Background(), sw.ContextAPIKey, sw.APIKey{
    Key: "APIKEY",
    Prefix: "Bearer", // Omit if not necessary.
})
r, err := client.Service.Operation(auth, args)
```



## Author

feedback@opswat.com
