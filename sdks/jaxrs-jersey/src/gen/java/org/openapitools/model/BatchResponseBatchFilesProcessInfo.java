/*
 * MetaDefender Core
 * ## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 
 *
 * The version of the OpenAPI document: v4.18.0
 * Contact: feedback@opswat.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import javax.validation.constraints.*;
import javax.validation.Valid;

/**
 * The analysis summary
 */
@ApiModel(description = "The analysis summary")
@JsonPropertyOrder({
  BatchResponseBatchFilesProcessInfo.JSON_PROPERTY_BLOCKED_REASON,
  BatchResponseBatchFilesProcessInfo.JSON_PROPERTY_PROGRESS_PERCENTAGE,
  BatchResponseBatchFilesProcessInfo.JSON_PROPERTY_RESULT,
  BatchResponseBatchFilesProcessInfo.JSON_PROPERTY_VERDICTS
})
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaJerseyServerCodegen", date = "2020-05-15T23:49:49.064488Z[UTC]")
public class BatchResponseBatchFilesProcessInfo   {
  public static final String JSON_PROPERTY_BLOCKED_REASON = "blocked_reason";
  @JsonProperty(JSON_PROPERTY_BLOCKED_REASON)
  private String blockedReason;

  public static final String JSON_PROPERTY_PROGRESS_PERCENTAGE = "progress_percentage";
  @JsonProperty(JSON_PROPERTY_PROGRESS_PERCENTAGE)
  private Integer progressPercentage;

  public static final String JSON_PROPERTY_RESULT = "result";
  @JsonProperty(JSON_PROPERTY_RESULT)
  private String result;

  public static final String JSON_PROPERTY_VERDICTS = "verdicts";
  @JsonProperty(JSON_PROPERTY_VERDICTS)
  private List<String> verdicts = null;

  public BatchResponseBatchFilesProcessInfo blockedReason(String blockedReason) {
    this.blockedReason = blockedReason;
    return this;
  }

  /**
   * Provides the reason why the file is blocked (if so).
   * @return blockedReason
   **/
  @JsonProperty("blocked_reason")
  @ApiModelProperty(example = "Infected", value = "Provides the reason why the file is blocked (if so).")
  
  public String getBlockedReason() {
    return blockedReason;
  }

  public void setBlockedReason(String blockedReason) {
    this.blockedReason = blockedReason;
  }

  public BatchResponseBatchFilesProcessInfo progressPercentage(Integer progressPercentage) {
    this.progressPercentage = progressPercentage;
    return this;
  }

  /**
   * Percentage of processing completed (from 1-100).
   * @return progressPercentage
   **/
  @JsonProperty("progress_percentage")
  @ApiModelProperty(example = "100", value = "Percentage of processing completed (from 1-100).")
  
  public Integer getProgressPercentage() {
    return progressPercentage;
  }

  public void setProgressPercentage(Integer progressPercentage) {
    this.progressPercentage = progressPercentage;
  }

  public BatchResponseBatchFilesProcessInfo result(String result) {
    this.result = result;
    return this;
  }

  /**
   * The final result of processing the file (Allowed / Blocked / Processing).
   * @return result
   **/
  @JsonProperty("result")
  @ApiModelProperty(example = "Blocked", value = "The final result of processing the file (Allowed / Blocked / Processing).")
  
  public String getResult() {
    return result;
  }

  public void setResult(String result) {
    this.result = result;
  }

  public BatchResponseBatchFilesProcessInfo verdicts(List<String> verdicts) {
    this.verdicts = verdicts;
    return this;
  }

  public BatchResponseBatchFilesProcessInfo addVerdictsItem(String verdictsItem) {
    if (this.verdicts == null) {
      this.verdicts = new ArrayList<String>();
    }
    this.verdicts.add(verdictsItem);
    return this;
  }

  /**
   * Aggregated list of potential issues.
   * @return verdicts
   **/
  @JsonProperty("verdicts")
  @ApiModelProperty(example = "[Infected]", value = "Aggregated list of potential issues.")
  
  public List<String> getVerdicts() {
    return verdicts;
  }

  public void setVerdicts(List<String> verdicts) {
    this.verdicts = verdicts;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BatchResponseBatchFilesProcessInfo batchResponseBatchFilesProcessInfo = (BatchResponseBatchFilesProcessInfo) o;
    return Objects.equals(this.blockedReason, batchResponseBatchFilesProcessInfo.blockedReason) &&
        Objects.equals(this.progressPercentage, batchResponseBatchFilesProcessInfo.progressPercentage) &&
        Objects.equals(this.result, batchResponseBatchFilesProcessInfo.result) &&
        Objects.equals(this.verdicts, batchResponseBatchFilesProcessInfo.verdicts);
  }

  @Override
  public int hashCode() {
    return Objects.hash(blockedReason, progressPercentage, result, verdicts);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BatchResponseBatchFilesProcessInfo {\n");
    
    sb.append("    blockedReason: ").append(toIndentedString(blockedReason)).append("\n");
    sb.append("    progressPercentage: ").append(toIndentedString(progressPercentage)).append("\n");
    sb.append("    result: ").append(toIndentedString(result)).append("\n");
    sb.append("    verdicts: ").append(toIndentedString(verdicts)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}
