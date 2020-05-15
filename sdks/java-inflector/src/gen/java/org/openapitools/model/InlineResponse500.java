package org.openapitools.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;





@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaInflectorServerCodegen", date = "2020-05-15T23:49:39.082677Z[UTC]")
public class InlineResponse500   {
  @JsonProperty("err")
  private String err;

  /**
   * Error reason
   **/
  public InlineResponse500 err(String err) {
    this.err = err;
    return this;
  }

  
  @ApiModelProperty(value = "Error reason")
  @JsonProperty("err")
  public String getErr() {
    return err;
  }
  public void setErr(String err) {
    this.err = err;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InlineResponse500 inlineResponse500 = (InlineResponse500) o;
    return Objects.equals(err, inlineResponse500.err);
  }

  @Override
  public int hashCode() {
    return Objects.hash(err);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InlineResponse500 {\n");
    
    sb.append("    err: ").append(toIndentedString(err)).append("\n");
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
