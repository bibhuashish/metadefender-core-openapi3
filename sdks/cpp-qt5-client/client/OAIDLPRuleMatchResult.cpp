/**
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

#include "OAIDLPRuleMatchResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDLPRuleMatchResult::OAIDLPRuleMatchResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDLPRuleMatchResult::OAIDLPRuleMatchResult() {
    this->initializeModel();
}

OAIDLPRuleMatchResult::~OAIDLPRuleMatchResult() {}

void OAIDLPRuleMatchResult::initializeModel() {

    m_after_isSet = false;
    m_after_isValid = false;

    m_before_isSet = false;
    m_before_isValid = false;

    m_certainty_isSet = false;
    m_certainty_isValid = false;

    m_certainty_score_isSet = false;
    m_certainty_score_isValid = false;

    m_hit_isSet = false;
    m_hit_isValid = false;

    m_is_redacted_isSet = false;
    m_is_redacted_isValid = false;

    m_severity_isSet = false;
    m_severity_isValid = false;
}

void OAIDLPRuleMatchResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDLPRuleMatchResult::fromJsonObject(QJsonObject json) {

    m_after_isValid = ::OpenAPI::fromJsonValue(after, json[QString("after")]);
    m_after_isSet = !json[QString("after")].isNull() && m_after_isValid;

    m_before_isValid = ::OpenAPI::fromJsonValue(before, json[QString("before")]);
    m_before_isSet = !json[QString("before")].isNull() && m_before_isValid;

    m_certainty_isValid = ::OpenAPI::fromJsonValue(certainty, json[QString("certainty")]);
    m_certainty_isSet = !json[QString("certainty")].isNull() && m_certainty_isValid;

    m_certainty_score_isValid = ::OpenAPI::fromJsonValue(certainty_score, json[QString("certainty_score")]);
    m_certainty_score_isSet = !json[QString("certainty_score")].isNull() && m_certainty_score_isValid;

    m_hit_isValid = ::OpenAPI::fromJsonValue(hit, json[QString("hit")]);
    m_hit_isSet = !json[QString("hit")].isNull() && m_hit_isValid;

    m_is_redacted_isValid = ::OpenAPI::fromJsonValue(is_redacted, json[QString("isRedacted")]);
    m_is_redacted_isSet = !json[QString("isRedacted")].isNull() && m_is_redacted_isValid;

    m_severity_isValid = ::OpenAPI::fromJsonValue(severity, json[QString("severity")]);
    m_severity_isSet = !json[QString("severity")].isNull() && m_severity_isValid;
}

QString OAIDLPRuleMatchResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDLPRuleMatchResult::asJsonObject() const {
    QJsonObject obj;
    if (m_after_isSet) {
        obj.insert(QString("after"), ::OpenAPI::toJsonValue(after));
    }
    if (m_before_isSet) {
        obj.insert(QString("before"), ::OpenAPI::toJsonValue(before));
    }
    if (m_certainty_isSet) {
        obj.insert(QString("certainty"), ::OpenAPI::toJsonValue(certainty));
    }
    if (m_certainty_score_isSet) {
        obj.insert(QString("certainty_score"), ::OpenAPI::toJsonValue(certainty_score));
    }
    if (m_hit_isSet) {
        obj.insert(QString("hit"), ::OpenAPI::toJsonValue(hit));
    }
    if (m_is_redacted_isSet) {
        obj.insert(QString("isRedacted"), ::OpenAPI::toJsonValue(is_redacted));
    }
    if (m_severity_isSet) {
        obj.insert(QString("severity"), ::OpenAPI::toJsonValue(severity));
    }
    return obj;
}

QString OAIDLPRuleMatchResult::getAfter() const {
    return after;
}
void OAIDLPRuleMatchResult::setAfter(const QString &after) {
    this->after = after;
    this->m_after_isSet = true;
}

QString OAIDLPRuleMatchResult::getBefore() const {
    return before;
}
void OAIDLPRuleMatchResult::setBefore(const QString &before) {
    this->before = before;
    this->m_before_isSet = true;
}

QString OAIDLPRuleMatchResult::getCertainty() const {
    return certainty;
}
void OAIDLPRuleMatchResult::setCertainty(const QString &certainty) {
    this->certainty = certainty;
    this->m_certainty_isSet = true;
}

qint32 OAIDLPRuleMatchResult::getCertaintyScore() const {
    return certainty_score;
}
void OAIDLPRuleMatchResult::setCertaintyScore(const qint32 &certainty_score) {
    this->certainty_score = certainty_score;
    this->m_certainty_score_isSet = true;
}

QString OAIDLPRuleMatchResult::getHit() const {
    return hit;
}
void OAIDLPRuleMatchResult::setHit(const QString &hit) {
    this->hit = hit;
    this->m_hit_isSet = true;
}

bool OAIDLPRuleMatchResult::isIsRedacted() const {
    return is_redacted;
}
void OAIDLPRuleMatchResult::setIsRedacted(const bool &is_redacted) {
    this->is_redacted = is_redacted;
    this->m_is_redacted_isSet = true;
}

qint32 OAIDLPRuleMatchResult::getSeverity() const {
    return severity;
}
void OAIDLPRuleMatchResult::setSeverity(const qint32 &severity) {
    this->severity = severity;
    this->m_severity_isSet = true;
}

bool OAIDLPRuleMatchResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_after_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_before_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_certainty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_certainty_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_redacted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_severity_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDLPRuleMatchResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI