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
import com.fasterxml.jackson.annotation.JsonValue;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import org.openapitools.model.DLPResponseDlpInfoHits;
import org.openapitools.model.DLPResponseDlpInfoMetadataRemoval;
import org.openapitools.model.DLPResponseDlpInfoRedact;
import org.openapitools.model.DLPResponseDlpInfoWatermark;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import javax.validation.constraints.*;
import javax.validation.Valid;

/**
 * Information on matched sensitive data
 */
@ApiModel(description = "Information on matched sensitive data")
@JsonPropertyOrder({
  DLPResponseDlpInfo.JSON_PROPERTY_CERTAINTY,
  DLPResponseDlpInfo.JSON_PROPERTY_ERRORS,
  DLPResponseDlpInfo.JSON_PROPERTY_FILENAME,
  DLPResponseDlpInfo.JSON_PROPERTY_HITS,
  DLPResponseDlpInfo.JSON_PROPERTY_METADATA_REMOVAL,
  DLPResponseDlpInfo.JSON_PROPERTY_REDACT,
  DLPResponseDlpInfo.JSON_PROPERTY_SEVERITY,
  DLPResponseDlpInfo.JSON_PROPERTY_VERDICT,
  DLPResponseDlpInfo.JSON_PROPERTY_WATERMARK
})
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaJerseyServerCodegen", date = "2020-05-15T23:49:49.064488Z[UTC]")
public class DLPResponseDlpInfo   {
  /**
   * Describes how certain the hit is, possible values:   * &#x60;Very Low&#x60;   * &#x60;Low&#x60;   * &#x60;Medium&#x60;   * &#x60;High&#x60;   * &#x60;Very High&#x60; 
   */
  public enum CertaintyEnum {
    VERY_LOW("Very Low"),
    
    LOW("Low"),
    
    MEDIUM("Medium"),
    
    HIGH("High"),
    
    VERY_HIGH("Very High");

    private String value;

    CertaintyEnum(String value) {
      this.value = value;
    }

    @Override
    @JsonValue
    public String toString() {
      return String.valueOf(value);
    }

    @JsonCreator
    public static CertaintyEnum fromValue(String value) {
      for (CertaintyEnum b : CertaintyEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }
  }

  public static final String JSON_PROPERTY_CERTAINTY = "certainty";
  @JsonProperty(JSON_PROPERTY_CERTAINTY)
  private CertaintyEnum certainty;

  public static final String JSON_PROPERTY_ERRORS = "errors";
  @JsonProperty(JSON_PROPERTY_ERRORS)
  private Object errors;

  public static final String JSON_PROPERTY_FILENAME = "filename";
  @JsonProperty(JSON_PROPERTY_FILENAME)
  private String filename;

  public static final String JSON_PROPERTY_HITS = "hits";
  @JsonProperty(JSON_PROPERTY_HITS)
  private DLPResponseDlpInfoHits hits;

  public static final String JSON_PROPERTY_METADATA_REMOVAL = "metadata_removal";
  @JsonProperty(JSON_PROPERTY_METADATA_REMOVAL)
  private DLPResponseDlpInfoMetadataRemoval metadataRemoval;

  public static final String JSON_PROPERTY_REDACT = "redact";
  @JsonProperty(JSON_PROPERTY_REDACT)
  private DLPResponseDlpInfoRedact redact;

  /**
   * (NOTE: this field is deprecated): represents the severity of the data loss, possible values:   * &#x60;0&#x60; - Certainly is data loss   * &#x60;1&#x60; - Might be data loss 
   */
  public enum SeverityEnum {
    NUMBER_0(0),
    
    NUMBER_1(1);

    private Integer value;

    SeverityEnum(Integer value) {
      this.value = value;
    }

    @Override
    @JsonValue
    public String toString() {
      return String.valueOf(value);
    }

    @JsonCreator
    public static SeverityEnum fromValue(Integer value) {
      for (SeverityEnum b : SeverityEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }
  }

  public static final String JSON_PROPERTY_SEVERITY = "severity";
  @JsonProperty(JSON_PROPERTY_SEVERITY)
  private SeverityEnum severity;

  /**
   * The overall result for the scanned file. It can be   | index         | status                       |   |---------------|------------------------------|   | 0             | Clean                        |   | 1             | Found matched data           |   | 2             | Suspicious                   |   | 3             | Failed                       |   | 4             | Not scanned                  | 
   */
  public enum VerdictEnum {
    NUMBER_0(0),
    
    NUMBER_1(1),
    
    NUMBER_2(2),
    
    NUMBER_3(3),
    
    NUMBER_4(4);

    private Integer value;

    VerdictEnum(Integer value) {
      this.value = value;
    }

    @Override
    @JsonValue
    public String toString() {
      return String.valueOf(value);
    }

    @JsonCreator
    public static VerdictEnum fromValue(Integer value) {
      for (VerdictEnum b : VerdictEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }
  }

  public static final String JSON_PROPERTY_VERDICT = "verdict";
  @JsonProperty(JSON_PROPERTY_VERDICT)
  private VerdictEnum verdict;

  public static final String JSON_PROPERTY_WATERMARK = "watermark";
  @JsonProperty(JSON_PROPERTY_WATERMARK)
  private DLPResponseDlpInfoWatermark watermark;

  public DLPResponseDlpInfo certainty(CertaintyEnum certainty) {
    this.certainty = certainty;
    return this;
  }

  /**
   * Describes how certain the hit is, possible values:   * &#x60;Very Low&#x60;   * &#x60;Low&#x60;   * &#x60;Medium&#x60;   * &#x60;High&#x60;   * &#x60;Very High&#x60; 
   * @return certainty
   **/
  @JsonProperty("certainty")
  @ApiModelProperty(example = "High", value = "Describes how certain the hit is, possible values:   * `Very Low`   * `Low`   * `Medium`   * `High`   * `Very High` ")
  
  public CertaintyEnum getCertainty() {
    return certainty;
  }

  public void setCertainty(CertaintyEnum certainty) {
    this.certainty = certainty;
  }

  public DLPResponseDlpInfo errors(Object errors) {
    this.errors = errors;
    return this;
  }

  /**
   * A  list of error objects (empty if no errors happened), each error object contains following keys:   * &#x60;scan&#x60;: scan related error description   * &#x60;redact&#x60;: redaction related error description   * &#x60;watermark&#x60;: watermark related error description   * &#x60;metadata_removal&#x60;: metadata removal related error description 
   * @return errors
   **/
  @JsonProperty("errors")
  @ApiModelProperty(example = "{redact=File structure invalid.}", value = "A  list of error objects (empty if no errors happened), each error object contains following keys:   * `scan`: scan related error description   * `redact`: redaction related error description   * `watermark`: watermark related error description   * `metadata_removal`: metadata removal related error description ")
  @Valid 
  public Object getErrors() {
    return errors;
  }

  public void setErrors(Object errors) {
    this.errors = errors;
  }

  public DLPResponseDlpInfo filename(String filename) {
    this.filename = filename;
    return this;
  }

  /**
   * Output processed file name (pre-configured on engine settings under Core&#39;s worflow rule)
   * @return filename
   **/
  @JsonProperty("filename")
  @ApiModelProperty(example = "OPSWAT_Proactive_DLP_CCN_proactive-dlp-processed_by_OPSWAT_MetaDefender_8101abae27be4d63859c55d9e0ed0135.pdf", value = "Output processed file name (pre-configured on engine settings under Core's worflow rule)")
  
  public String getFilename() {
    return filename;
  }

  public void setFilename(String filename) {
    this.filename = filename;
  }

  public DLPResponseDlpInfo hits(DLPResponseDlpInfoHits hits) {
    this.hits = hits;
    return this;
  }

  /**
   * Get hits
   * @return hits
   **/
  @JsonProperty("hits")
  @ApiModelProperty(value = "")
  @Valid 
  public DLPResponseDlpInfoHits getHits() {
    return hits;
  }

  public void setHits(DLPResponseDlpInfoHits hits) {
    this.hits = hits;
  }

  public DLPResponseDlpInfo metadataRemoval(DLPResponseDlpInfoMetadataRemoval metadataRemoval) {
    this.metadataRemoval = metadataRemoval;
    return this;
  }

  /**
   * Get metadataRemoval
   * @return metadataRemoval
   **/
  @JsonProperty("metadata_removal")
  @ApiModelProperty(value = "")
  @Valid 
  public DLPResponseDlpInfoMetadataRemoval getMetadataRemoval() {
    return metadataRemoval;
  }

  public void setMetadataRemoval(DLPResponseDlpInfoMetadataRemoval metadataRemoval) {
    this.metadataRemoval = metadataRemoval;
  }

  public DLPResponseDlpInfo redact(DLPResponseDlpInfoRedact redact) {
    this.redact = redact;
    return this;
  }

  /**
   * Get redact
   * @return redact
   **/
  @JsonProperty("redact")
  @ApiModelProperty(value = "")
  @Valid 
  public DLPResponseDlpInfoRedact getRedact() {
    return redact;
  }

  public void setRedact(DLPResponseDlpInfoRedact redact) {
    this.redact = redact;
  }

  public DLPResponseDlpInfo severity(SeverityEnum severity) {
    this.severity = severity;
    return this;
  }

  /**
   * (NOTE: this field is deprecated): represents the severity of the data loss, possible values:   * &#x60;0&#x60; - Certainly is data loss   * &#x60;1&#x60; - Might be data loss 
   * @return severity
   **/
  @JsonProperty("severity")
  @ApiModelProperty(example = "0", value = "(NOTE: this field is deprecated): represents the severity of the data loss, possible values:   * `0` - Certainly is data loss   * `1` - Might be data loss ")
  
  public SeverityEnum getSeverity() {
    return severity;
  }

  public void setSeverity(SeverityEnum severity) {
    this.severity = severity;
  }

  public DLPResponseDlpInfo verdict(VerdictEnum verdict) {
    this.verdict = verdict;
    return this;
  }

  /**
   * The overall result for the scanned file. It can be   | index         | status                       |   |---------------|------------------------------|   | 0             | Clean                        |   | 1             | Found matched data           |   | 2             | Suspicious                   |   | 3             | Failed                       |   | 4             | Not scanned                  | 
   * @return verdict
   **/
  @JsonProperty("verdict")
  @ApiModelProperty(example = "1", value = "The overall result for the scanned file. It can be   | index         | status                       |   |---------------|------------------------------|   | 0             | Clean                        |   | 1             | Found matched data           |   | 2             | Suspicious                   |   | 3             | Failed                       |   | 4             | Not scanned                  | ")
  
  public VerdictEnum getVerdict() {
    return verdict;
  }

  public void setVerdict(VerdictEnum verdict) {
    this.verdict = verdict;
  }

  public DLPResponseDlpInfo watermark(DLPResponseDlpInfoWatermark watermark) {
    this.watermark = watermark;
    return this;
  }

  /**
   * Get watermark
   * @return watermark
   **/
  @JsonProperty("watermark")
  @ApiModelProperty(value = "")
  @Valid 
  public DLPResponseDlpInfoWatermark getWatermark() {
    return watermark;
  }

  public void setWatermark(DLPResponseDlpInfoWatermark watermark) {
    this.watermark = watermark;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DLPResponseDlpInfo dlPResponseDlpInfo = (DLPResponseDlpInfo) o;
    return Objects.equals(this.certainty, dlPResponseDlpInfo.certainty) &&
        Objects.equals(this.errors, dlPResponseDlpInfo.errors) &&
        Objects.equals(this.filename, dlPResponseDlpInfo.filename) &&
        Objects.equals(this.hits, dlPResponseDlpInfo.hits) &&
        Objects.equals(this.metadataRemoval, dlPResponseDlpInfo.metadataRemoval) &&
        Objects.equals(this.redact, dlPResponseDlpInfo.redact) &&
        Objects.equals(this.severity, dlPResponseDlpInfo.severity) &&
        Objects.equals(this.verdict, dlPResponseDlpInfo.verdict) &&
        Objects.equals(this.watermark, dlPResponseDlpInfo.watermark);
  }

  @Override
  public int hashCode() {
    return Objects.hash(certainty, errors, filename, hits, metadataRemoval, redact, severity, verdict, watermark);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DLPResponseDlpInfo {\n");
    
    sb.append("    certainty: ").append(toIndentedString(certainty)).append("\n");
    sb.append("    errors: ").append(toIndentedString(errors)).append("\n");
    sb.append("    filename: ").append(toIndentedString(filename)).append("\n");
    sb.append("    hits: ").append(toIndentedString(hits)).append("\n");
    sb.append("    metadataRemoval: ").append(toIndentedString(metadataRemoval)).append("\n");
    sb.append("    redact: ").append(toIndentedString(redact)).append("\n");
    sb.append("    severity: ").append(toIndentedString(severity)).append("\n");
    sb.append("    verdict: ").append(toIndentedString(verdict)).append("\n");
    sb.append("    watermark: ").append(toIndentedString(watermark)).append("\n");
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
