import React from 'react';
import './PropertyHeader.css';

export interface PropertyHeaderProps {
  title: string;
  location: {
    neighborhood: string;
    city: string;
  };
  propertyType: string;
  maxGuests: number;
  className?: string;
}

const PropertyHeader: React.FC<PropertyHeaderProps> = ({
  title,
  location,
  propertyType,
  maxGuests,
  className,
}) => {
  return (
    <div className={`property-header${className ? ' ' + className : ''}`}>
      <h1 className="property-title">{title}</h1>

      <div className="property-location">
        <svg
          className="map-pin-icon"
          width="16"
          height="20"
          viewBox="0 0 16 20"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
        >
          <path
            d="M8 0C3.58 0 0 3.58 0 8C0 12 8 20 8 20C8 20 16 12 16 8C16 3.58 12.42 0 8 0ZM8 11C6.34 11 5 9.66 5 8C5 6.34 6.34 5 8 5C9.66 5 11 6.34 11 8C11 9.66 9.66 11 8 11Z"
            fill="currentColor"
          />
        </svg>
        <span className="location-text">
          Located in {location.neighborhood}, {location.city}
        </span>
      </div>

      <div className="property-details">
        {propertyType} - {maxGuests} guest{maxGuests !== 1 ? 's' : ''} max
      </div>
    </div>
  );
};

export default PropertyHeader;
