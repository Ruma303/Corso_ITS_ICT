package itc.ebuy.models;

public class CompraloSubito extends Post {

    private CompraloSubito(Builder b) {
        super(b);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static class Builder extends Post.Builder<Builder> {

        @Override
        protected Builder self() {
            return this;
        }

        @Override
        public CompraloSubito build() {
            return new CompraloSubito(this);
        }
    }
}