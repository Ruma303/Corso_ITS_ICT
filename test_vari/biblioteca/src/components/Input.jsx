export default function Input({
  id,
  name,
  label,
  type = "text",
  placeholder,
  value,
  onChange,
  ...props
}) {
  return (
    <div>
      <label htmlFor={id}>{label}</label>
      
      <input
        id={id}
        name={name}
        type={type}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
        {...props}
      />
    </div>
  );
}